from __future__ import annotations

from .email_selector import EmailSelectorAny
from .email_selector.resource_selector import EmailSelector
from .logger import Logger
from .models import Email, GetEmailRequest, Resource
from .rule_evaluator import RuleEvaluator
from .usage_checker import UsageChecker


class EmailAddressGetter:
    def __init__(
        self,
        rule_evaluator: RuleEvaluator,
        usage_checker: UsageChecker,
        email_selector: EmailSelectorAny,
        logger: Logger,
    ) -> None:
        self._rule_evaluator = rule_evaluator
        self._usage_checker = usage_checker
        self._email_selector = email_selector
        self._logger = logger

    def get_email_address(self, request: GetEmailRequest) -> Email | None:
        if candidate := self._check_candidates(request):
            return candidate

        return self._select_email(request)

    def _check_candidates(self, request: GetEmailRequest) -> Email | None:
        if not request.candidates:
            self._logger.info("No candidates provided")
            return None

        usable_candidates = self._rule_evaluator.get_usable_candidates(
            request.candidates
        )

        if not usable_candidates:
            self._logger.info("No usable candidates")
            return None

        # TODO filter usable candidates by with usage limits
        if not self._usage_checker.is_usage_within_limits(request):
            return None

        # TODO logging / measurement about number of usable candidates
        return usable_candidates[0].email

    def _select_email(self, request: GetEmailRequest) -> Email | None:
        return self._email_selector.select_email(request)
