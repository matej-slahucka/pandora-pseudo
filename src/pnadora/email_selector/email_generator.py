from ..models import Algorithm, AlgorithmData, Email


class EmailGenerator:
    def __init__(
        self,
        domain_name: str,
        booking_id: int,
        algorithm_name: Algorithm,
        algorithm_data: AlgorithmData,
    ) -> None:
        self.domain_name = domain_name
        self.booking_id = booking_id
        self.algorithm_name = algorithm_name
        self.algorithm_data = algorithm_data

        self.algorithm_config = {
            Algorithm.BID: self._generate_from_booking_id,
            Algorithm.NAME_SURNAME_NUM: self._generate_from_full,
            Algorithm.SHORTENED_NAME: self._generate_short_name,
        }

    def generate_email(self) -> Email:
        email = self.algorithm_config[self.algorithm_name]()
        return Email(name=email.name.lower(), domain=email.domain.lower())

    def _generate_from_booking_id(self) -> Email:
        return Email(name=str(self.booking_id), domain=self.domain_name)

    def _generate_from_full(self) -> Email:
        firstname = self.algorithm_data.name
        surname = self.algorithm_data.surname
        number = self.algorithm_data.number

        return Email(name=f"{firstname}{surname}{number}", domain=self.domain_name)

    def _generate_short_name(self) -> Email:
        firstname = self.algorithm_data.name
        surname = self.algorithm_data.surname
        length = self.algorithm_data.number

        candidate = f"{firstname}{surname}"[:length]
        return Email(name=candidate, domain=self.domain_name)
