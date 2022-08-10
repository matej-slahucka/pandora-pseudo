from typing import TypeGuard

from ..models import Domain, Email, GetEmailRequest, GetEmailRequestDomain, Resource
from .resource_selector import EmailSelector


class BookingIdEmailSelector(EmailSelector[Domain, GetEmailRequestDomain]):
    def _create_email(self, resource: Domain, request: GetEmailRequestDomain) -> Email:
        return Email(name=str(request.booking_id), domain=resource.domain)

    def _can_create(self, resource: Resource) -> TypeGuard[Domain]:
        return isinstance(resource, Domain)

    def _can_process_request(
        self, request: GetEmailRequest
    ) -> TypeGuard[GetEmailRequestDomain]:
        return isinstance(request, GetEmailRequestDomain)
