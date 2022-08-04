from abc import ABC, abstractmethod

from ..models import Rule, Tier


class RuleRepository(ABC):
    @abstractmethod
    def get_rules(self, tier: Tier) -> list[Rule]:
        ...
