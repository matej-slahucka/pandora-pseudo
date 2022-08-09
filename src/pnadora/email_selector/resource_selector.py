from abc import ABC, abstractmethod
from dataclasses import asdict
from typing import Generic, TypeGuard, TypeVar, final

from ..logger import Logger
from ..models import Email, GetEmailRequest, Resource, Rule
from ..repositories import ResourceRepository

T = TypeVar("T", bound=Resource)
U = TypeVar("U", bound=GetEmailRequest)


class EmailSelectorError(Exception):
    pass


class RuleNotFoundError(EmailSelectorError):
    pass


class UnexpectedRequestError(EmailSelectorError):
    pass


class UnexpectedResourceError(EmailSelectorError):
    pass


class EmailSelector(ABC, Generic[T, U]):
    def __init__(self, resource_repository: ResourceRepository, logger: Logger) -> None:
        self._resource_repository = resource_repository
        self._logger = logger

    @final
    def select_email(self, request: GetEmailRequest) -> Email | None:
        rules = self._resource_repository.get_rules(request.channel, request.carrier)

        if not rules:
            self._logger.warn("No rules matched")
            raise RuleNotFoundError

        email = None

        for rule in rules:
            email = self._get_email_by_rule(rule, request)

            if email is not None:
                break

        return email

    @final
    def _get_email_by_rule(self, rule: Rule, request: GetEmailRequest) -> Email | None:
        resources_with_usage = self._resource_repository.get_emails_by_usage(
            request, rule
        )

        if not resources_with_usage:
            self._logger.warn("No domains for rule", rule=rule.name)
            return None

        resource_with_usage = resources_with_usage[0]
        if resource_with_usage.frequency >= rule.frequency:
            self._logger.warn("All domains for rule used", rule=rule.name)
            return None

        resource = resource_with_usage.resource

        # TODO: abstract away email from account vs email from domains using the generator
        self._logger.info(
            "resource_selected",
            rule=rule.name,
            resource=asdict(resource_with_usage.resource),
        )

        if not self._can_process_request(request):
            raise UnexpectedRequestError

        if not self._can_create(resource):
            raise UnexpectedResourceError

        email = self._create_email(resource, request)
        self._resource_repository.save_usage(email, request)

        return email

    @abstractmethod
    def _create_email(self, resource: T, request: U) -> Email:
        ...

    @abstractmethod
    def _can_create(self, resource: Resource) -> TypeGuard[T]:
        ...

    @abstractmethod
    def _can_process_request(self, request: GetEmailRequest) -> TypeGuard[U]:
        ...
