from pnadora.email_selector.booking_id_email_selector import BookingIdEmailSelector

from ..email_selector.domain_selector import FromDomainSelector
from ..logger import Logger
from ..models import Domain, Email, GetEmailRequestDomain, GetEmailRequestEmail, Tier
from ..repositories.email_repository import ResourceRepository
from .email_selector import FromEmailSelector
from .resource_selector import EmailSelector

EmailSelectorAny = (
    EmailSelector[Email, GetEmailRequestEmail]
    | EmailSelector[Domain, GetEmailRequestDomain]
)


class EmailSelectorFactory:
    def __init__(
        self,
        domain_repository: ResourceRepository,
        email_repository: ResourceRepository,
        logger: Logger,
    ) -> None:
        self._domain_repository = domain_repository
        self._email_repository = email_repository
        self._logger = logger

    def create_email_selector(self, tier: Tier) -> EmailSelectorAny:
        match tier:
            case Tier.TIER1:
                return BookingIdEmailSelector(self._domain_repository, self._logger)
            case Tier.TIER2:
                return FromDomainSelector(self._domain_repository, self._logger)
            case Tier.TIER3:
                return FromEmailSelector(self._email_repository, self._logger)
