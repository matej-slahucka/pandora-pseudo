from ..models import Tier
from .account_email_repository import AccountEmailRepository
from .domain_email_repository import DomainEmailRepository
from .email_repository import ResourceRepository


class EmailRepositoryFactory:
    TIER_TO_RULE_REPOSITORY = {
        Tier.TIER1: DomainEmailRepository,
        Tier.TIER2: DomainEmailRepository,
        Tier.TIER3: AccountEmailRepository,
    }

    def create_email_repository(self, tier: Tier) -> ResourceRepository:
        return self.TIER_TO_RULE_REPOSITORY[tier]()
