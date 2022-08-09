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
    def get_rules(self, channel: Channel, carrier: Carrier) -> list[Rule]:
        ...

    @abstractmethod
    def get_emails_by_usage(
        self, request: GetEmailRequest, rule: Rule
    ) -> list[ResourceWithUsage]:
        ...

    @abstractmethod
    def save_usage(
        self, email: Email, request: GetEmailRequest
    ) -> list[ResourceWithUsage]:
        ...

    @abstractmethod
    def get_usage(self) -> None:
        ...
