from __future__ import annotations

from .email_address_getter import EmailAddressGetter
from .email_selector import EmailSelectorFactory
from .logger import Logger
from .models import Email, GetEmailRequest
from .repositories import EmailRepositoryFactory
from .rule_evaluator import RuleEvaluator
from .usage_checker import UsageCheckerFactory


class GetEmailAddressError(Exception):
    pass


class GetEmailAddressController:
    def __init__(
        self,
        email_repository_factory: EmailRepositoryFactory,
        usage_checker_factory: UsageCheckerFactory,
        email_selector_factory: EmailSelectorFactory,
        logger: Logger,
    ) -> None:
        self._email_repository_factory = email_repository_factory
        self._usage_checker_factory = usage_checker_factory
        self._email_selector_factory = email_selector_factory
        self._logger = logger

    def _create_email_address_getter(
        self, request: GetEmailRequest
    ) -> EmailAddressGetter:
        rule_repository = self._email_repository_factory.create_email_repository(
            request.tier
        )

        rule_evaluator = RuleEvaluator(rule_repository)
        usage_checker = self._usage_checker_factory.create_usage_checker(request.tier)
        email_selector = self._email_selector_factory.create_email_selector(
            request.tier
        )

        return EmailAddressGetter(
            rule_evaluator, usage_checker, email_selector, self._logger
        )

    def get_email_address_use_case(self, request: GetEmailRequest) -> Email:
        email_address_getter = self._create_email_address_getter(request)
        email = email_address_getter.get_email_address(request)

        if email is None:
            raise GetEmailAddressError

        return email
