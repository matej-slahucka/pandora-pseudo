from ...models import AlgorithmData, Email
from .email_algorithm_generator import EmailAlgorithmGenerator


class FullNameEmailGenerator(EmailAlgorithmGenerator):
    def __init__(self, algorithm_data: AlgorithmData, domain_name: str) -> None:
        self._algorithm_data = algorithm_data
        self._domain_name = domain_name

    def generate(self) -> Email:
        firstname = self._algorithm_data.name
        surname = self._algorithm_data.surname
        number = self._algorithm_data.number

        return Email(name=f"{firstname}{surname}{number}", domain=self._domain_name)
