from .models import Email
from .rule_repository import RuleRepository


class RuleEvaluator:
    def __init__(self, rule_repository: RuleRepository) -> None:
        self._rule_repository = rule_repository

    def email_can_be_used(self, email: Email) -> bool:
        raise NotImplemented
