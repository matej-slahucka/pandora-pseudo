from abc import ABC, abstractmethod

from ..models import (
    Carrier,
    Channel,
    Email,
    EmailWithUsage,
    GetEmailRequest,
    Rule,
    StoredEmail,
)


class RuleRepository(ABC):
    @abstractmethod
    def find_emails(self, emails: list[Email]) -> list[StoredEmail]:
        ...

    @abstractmethod
    def get_rules(self, channel: Channel, carrier: Carrier) -> list[Rule]:
        ...

    @abstractmethod
    def get_emails_by_usage(
        self, request: GetEmailRequest, rule: Rule
    ) -> list[EmailWithUsage]:
        ...

    @abstractmethod
    def save_usage(
        self, email: Email, request: GetEmailRequest
    ) -> list[EmailWithUsage]:
        ...
