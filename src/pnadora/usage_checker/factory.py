from ..logger import Logger
from ..models import Tier
from ..repositories import UsageRepository
from .always_allowing_usage_checker import AlwaysAllowingUsageChecker
from .counting_usage_checker import CountingUsageChecker
from .usage_checker import UsageChecker


class UsageCheckerFactory:
    def __init__(
        self,
        logger: Logger,
        domain_usage_repository: UsageRepository,
        account_usage_repository: UsageRepository,
    ) -> None:
        self._logger = logger
        self._domain_usage_repository = domain_usage_repository
        self._account_usage_repository = account_usage_repository

    def create_usage_checker(self, tier: Tier) -> UsageChecker:
        match tier:
            case Tier.TIER1:
                return AlwaysAllowingUsageChecker(self._logger)
            case Tier.TIER2:
                return CountingUsageChecker(self._domain_usage_repository)
            case Tier.TIER3:
                return CountingUsageChecker(self._account_usage_repository)
