from abc import ABC, abstractmethod

from ..models import (
    Carrier,
    Channel,
    Email,
    GetEmailRequest,
    ResourceWithUsage,
    Rule,
    StoredEmail,
)


class ResourceRepository(ABC):
    @abstractmethod
    def find_emails(self, emails: list[Email]) -> list[StoredEmail]:
        ...

    @abstractmethod
    def get_rules_sorted_by_usage(
        self, channel: Channel, carrier: Carrier
    ) -> list[Rule]:
        ...

    @abstractmethod
    def get_resource_with_usage_by_rule(
        self, request: GetEmailRequest, rule: Rule
    ) -> ResourceWithUsage | None:
        ...

    @abstractmethod
    def save_usage(self, email: Email, request: GetEmailRequest) -> None:
        ...

    @abstractmethod
    def get_usage(self) -> None:
        ...
