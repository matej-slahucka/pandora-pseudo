from ..models import GetEmailRequest
from ..repositories import EmailRepository
from .usage_checker import UsageChecker


class CountingUsageChecker(UsageChecker):
    def __init__(self, email_repository: EmailRepository):
        self._email_repository = email_repository

    def is_usage_within_limits(self, request: GetEmailRequest) -> bool:
        # query
        raise NotImplemented
