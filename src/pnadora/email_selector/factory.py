from ..models import GetEmailRequest, Resource, Tier
from .resource_selector import EmailSelector


class EmailSelectorFactory:
    def create_email_selector(
        self, tier: Tier
    ) -> EmailSelector[Resource, GetEmailRequest]:
        match tier:
            case Tier.TIER1:
                raise NotImplemented
            case Tier.TIER2:
                raise NotImplemented
            case Tier.TIER3:
                raise NotImplemented
