from .usage_repository import UsageRepository


class DomainUsageRepository(UsageRepository):
    def get_usage(self) -> None:
        raise NotImplemented
