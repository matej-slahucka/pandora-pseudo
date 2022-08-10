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
        raise NotImplementedError

    def get_rules_sorted_by_usage(
        self, channel: Channel, carrier: Carrier
    ) -> list[Rule]:
        raise NotImplementedError

    def get_resource_with_usage_by_rule(
        self, request: GetEmailRequest, rule: Rule
    ) -> ResourceWithUsage | None:
        raise NotImplementedError

    def save_usage(self, email: Email, request: GetEmailRequest) -> None:
        raise NotImplementedError

    def get_usage(self) -> None:
        raise NotImplementedError
