from __future__ import annotations

from .models import Email, GetEmailRequest
from .rule_evaluator import RuleEvaluator
from .usage_checker import UsageChecker
from .email_selector import EmailSelector


class EmailAddressGetter:
  def __init__(self, rule_evaluator: RuleEvaluator, usage_checker: UsageChecker, email_selector: EmailSelector) -> None:
    self._rule_evaluator = rule_evaluator
    self._usage_checker = usage_checker
    self._email_selector = email_selector

  def get_email_address(self, request: GetEmailRequest) -> Email | None:
    if request.candidate and (candidate := self._check_candidate(request)):
      return candidate

    return self._select_email(request)

  def _check_candidate(self, request: GetEmailRequest) -> Email | None:
    if not self._rule_evaluator.email_can_be_used(request.candidate):
      return None

    if not self._usage_checker.is_usage_within_limits(request):
      return None

    return request.candidate

  def _select_email(self, request: GetEmailRequest)  -> Email | None:
    return self._email_selector.select_email(request)
