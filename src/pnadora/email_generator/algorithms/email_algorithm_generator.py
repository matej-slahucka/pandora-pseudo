from abc import ABC, abstractmethod

from src.pnadora.models import Email


class EmailAlgorithmGenerator(ABC):
    @abstractmethod
    def generate(self) -> Email:
        ...
