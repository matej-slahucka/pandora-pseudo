from .usage_repository import UsageRepository


class AccountUsageRepository(UsageRepository):
    def get_usage(self) -> None:
        raise NotImplemented
