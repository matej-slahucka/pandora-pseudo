from ..logger import Logger
from ..models import Tier
from ..repositories import EmailRepository
from .always_allowing_usage_checker import AlwaysAllowingUsageChecker
from .counting_usage_checker import CountingUsageChecker
from .usage_checker import UsageChecker


class UsageCheckerFactory:
    def __init__(
        self,
        logger: Logger,
        domain_email_repository: EmailRepository,
        account_email_repository: EmailRepository,
    ) -> None:
        self._logger = logger
        self._domain_email_repository = domain_email_repository
        self._account_email_repository = account_email_repository

    def create_usage_checker(self, tier: Tier) -> UsageChecker:
        match tier:
            case Tier.TIER1:
                return AlwaysAllowingUsageChecker(self._logger)
            case Tier.TIER2:
                return CountingUsageChecker(self._domain_email_repository)
            case Tier.TIER3:
                return CountingUsageChecker(self._account_email_repository)
