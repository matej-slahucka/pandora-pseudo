from ..models import Tier, Rule
from .rule_repository import RuleRepository


class DomainRuleRepository(RuleRepository):
    def get_rules(self, tier: Tier) -> list[Rule]:
        raise NotImplemented
