from abc import ABC, abstractmethod

from .logger import Logger
from .models import GetEmailRequest, Tier
from .repositories import UsageRepository


class UsageChecker(ABC):
    @abstractmethod
    def is_usage_within_limits(self, request: GetEmailRequest) -> bool:
        ...


class AlwaysAllowingUsageChecker(UsageChecker):
    def __init__(self, logger: Logger) -> None:
        self._logger = logger

    def is_usage_within_limits(self, _: GetEmailRequest) -> bool:
        self._logger.info("Allowing usage")
        return True


class CountingUsageChecker(UsageChecker):
    def __init__(self, usage_repository: UsageRepository):
        self._usage_repository = usage_repository

    def is_usage_within_limits(self, request: GetEmailRequest) -> bool:
        # query
        raise NotImplemented


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
