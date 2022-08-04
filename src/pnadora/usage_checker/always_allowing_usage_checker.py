from ..logger import Logger
from ..models import GetEmailRequest
from .usage_checker import UsageChecker


class AlwaysAllowingUsageChecker(UsageChecker):
    def __init__(self, logger: Logger) -> None:
        self._logger = logger

    def is_usage_within_limits(self, _: GetEmailRequest) -> bool:
        self._logger.info("Allowing usage")
        return True
