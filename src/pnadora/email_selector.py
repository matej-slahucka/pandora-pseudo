from abc import ABC, abstractmethod

from .logger import Logger
from .models import Email, GetEmailRequest, Rule
from .repositories import EmailRepository


class RuleNotFoundError(Exception):
    pass


class EmailSelector(ABC):
    def __init__(self, email_repository: EmailRepository, logger: Logger) -> None:
        self._email_repository = email_repository
        self._logger = logger

    def select_email(self, request: GetEmailRequest) -> Email | None:
        rules = self._email_repository.get_rules(request.channel, request.carrier)

        if not rules:
            self._logger.warn("No rules matched")
            raise RuleNotFoundError

        email = None

        for rule in rules:
            email = self._get_email_by_rule(rule, request)

            if email is not None:
                break

        return email

    def _get_email_by_rule(self, rule: Rule, request: GetEmailRequest) -> Email | None:
        emails_with_usage = self._email_repository.get_emails_by_usage(request, rule)

        if not emails_with_usage:
            self._logger.warn("No domains for rule", rule=rule.name)
            return None

        email_with_usage = emails_with_usage[0]
        if email_with_usage.frequency >= rule.frequency:
            self._logger.warn("All domains for rule used", rule=rule.name)
            return None

        # TODO: abstract away email from account vs email from domains using the generator

        self._logger.info(
            "Email selected",
            rule=rule.name,
            email_name=email_with_usage.email.domain,
            email_domain=email_with_usage.email.domain,
        )

        email = self._create_email(email_with_usage.email)
        self._email_repository.save_usage(email, request)

        return email

    @abstractmethod
    def _create_email(self, email: Email) -> Email:
        # TODO: now this method doesn't really make sence because whole Email
        # structure won't be available in general.
        ...
