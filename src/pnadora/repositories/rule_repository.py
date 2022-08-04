from abc import ABC, abstractmethod

from ..models import Tier, Rule


class RuleRepository(ABC):
    @abstractmethod
    def get_rules(self, tier: Tier) -> list[Rule]:
        ...
