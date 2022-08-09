from typing import TypeGuard

from ..models import Domain, Email, GetEmailRequest, GetEmailRequestDomain, Resource
from .email_generator import EmailGenerator
from .resource_selector import EmailSelector


class FromDomainSelector(EmailSelector[Domain, GetEmailRequestDomain]):
    def _create_email(self, resource: Domain, request: GetEmailRequestDomain) -> Email:
        email_generator = EmailGenerator(
            resource.domain,
            request.booking_id,
            request.algorithm,
            request.algorithm_data,
        )
        return email_generator.generate_email()

    def _can_create(self, resource: Resource) -> TypeGuard[Domain]:
        return isinstance(resource, Domain)

    def _can_process_request(
        self, request: GetEmailRequest
    ) -> TypeGuard[GetEmailRequestDomain]:
        return isinstance(request, GetEmailRequestDomain)
