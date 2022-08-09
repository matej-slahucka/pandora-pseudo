from typing import TypeGuard

from ..models import Email, GetEmailRequest, GetEmailRequestEmail, Resource
from .resource_selector import EmailSelector


class FromEmailSelector(EmailSelector[Email, GetEmailRequestEmail]):
    def _create_email(self, resource: Email, _: GetEmailRequestEmail) -> Email:
        return resource

    def _can_create(self, resource: Resource) -> TypeGuard[Email]:
        return isinstance(resource, Email)

    def _can_process_request(
        self, request: GetEmailRequest
    ) -> TypeGuard[GetEmailRequestEmail]:
        return isinstance(request, GetEmailRequestEmail)
