from abc import ABC, abstractmethod
from .models import Email
from .rule_evaluator import RuleEvaluator


class CandidateChecker(ABC):
  @abstractmethod
  def can_use_candidate(self, candidate: Email) -> bool:
    ...


class BookingIdCandidateChecker(CandidateChecker):
  def __init__(self, rule_evaluator: RuleEvaluator) -> None:
    self._rule_evaluator = rule_evaluator

  def can_use_candidate(self, candidate: Email) -> bool:
    return self._rule_evaluator.email_can_be_used(candidate)


class Tier2CandidateChecker(CandidateChecker):
  def __init__(self, rule_evaluator: RuleEvaluator, usage_checker: UsageChecker) -> None:
    self._rule_evaluator = rule_evaluator
    self._usage_checker = usage_checker

  def can_use_candidate(self, candidate: Email) -> bool:
    can_be_used = self._rule_evaluator.email_can_be_used(candidate)
    usage_is_within_limits = self._usage_checker

    return can_be_used and usage_is_within_limits