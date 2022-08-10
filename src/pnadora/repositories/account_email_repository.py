from ..models import (
    Carrier,
    Channel,
    Email,
    GetEmailRequest,
    ResourceWithUsage,
    Rule,
    StoredEmail,
)
from .email_repository import ResourceRepository


class AccountEmailRepository(ResourceRepository):
    def find_emails(self, emails: list[Email]) -> list[StoredEmail]:
        raise NotImplemented

    def get_rules(self, channel: Channel, carrier: Carrier) -> list[Rule]:
        raise NotImplemented

    def get_emails_by_usage(
        self, request: GetEmailRequest, rule: Rule
    ) -> list[ResourceWithUsage]:
        raise NotImplemented

    def save_usage(
        self, email: Email, request: GetEmailRequest
    ) -> list[ResourceWithUsage]:
        raise NotImplemented

    def get_usage(self) -> None:
        raise NotImplemented
