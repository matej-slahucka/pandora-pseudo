from src.pnadora.models import Algorithm, AlgorithmData

from .algorithms.booking_id_email_generator import BookingIdEmailGenerator
from .algorithms.email_algorithm_generator import EmailAlgorithmGenerator
from .algorithms.full_name_email_generator import FullNameEmailGenerator
from .algorithms.shortened_name_email_generator import ShortenedNameEmailGenerator


class EmailAlgorithmGeneratorFactory:
    def __init__(
        self, booking_id: int, domain_name: str, algorithm_data: AlgorithmData
    ) -> None:
        self._domain_name = domain_name
        self._booking_id = booking_id
        self._algorithm_data = algorithm_data

    def create_email_generator(self, algorithm: Algorithm) -> EmailAlgorithmGenerator:
        match algorithm:
            case Algorithm.BID:
                return BookingIdEmailGenerator(self._booking_id, self._domain_name)
            case Algorithm.NAME_SURNAME_NUM:
                return FullNameEmailGenerator(self._algorithm_data, self._domain_name)
            case Algorithm.SHORTENED_NAME:
                return ShortenedNameEmailGenerator(
                    self._algorithm_data, self._domain_name
                )
