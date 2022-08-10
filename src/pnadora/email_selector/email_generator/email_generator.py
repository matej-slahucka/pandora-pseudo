from ...models import Algorithm, AlgorithmData, Email
from .email_algorithm_generator_factory import EmailAlgorithmGeneratorFactory


class EmailGenerator:
    def __init__(
        self,
        domain_name: str,
        booking_id: int,
        algorithm_name: Algorithm,
        algorithm_data: AlgorithmData,
    ) -> None:
        self._algorithm_name = algorithm_name
        self._algorithm_factory = EmailAlgorithmGeneratorFactory(
            booking_id, domain_name, algorithm_data
        )

    def generate_email(self) -> Email:
        email_generator = self._algorithm_factory.create_email_generator(
            self._algorithm_name
        )
        return email_generator.generate()
