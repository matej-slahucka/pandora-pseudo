from ...models import Email
from .email_algorithm_generator import EmailAlgorithmGenerator


class BookingIdEmailGenerator(EmailAlgorithmGenerator):
    def __init__(self, booking_id: int, domain_name: str) -> None:
        self._booking_id = booking_id
        self._domain_name = domain_name

    def generate(self) -> Email:
        return Email(name=str(self._booking_id), domain=self._domain_name)
