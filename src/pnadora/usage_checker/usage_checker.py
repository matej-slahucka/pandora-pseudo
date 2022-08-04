from abc import ABC, abstractmethod

from ..models import GetEmailRequest


class UsageChecker(ABC):
    @abstractmethod
    def is_usage_within_limits(self, request: GetEmailRequest) -> bool:
        ...
