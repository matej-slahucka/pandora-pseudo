from .repositories import UsageRepository
from .models import GetEmailRequest

class UsageChecker:
  def __init__(self, usage_repository: UsageRepository) -> None:
    self._usage_repository = usage_repository

  def is_usage_within_limits(self, request: GetEmailRequest) -> bool:
    # query
    raise NotImplemented