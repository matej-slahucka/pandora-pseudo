from abc import ABC, abstractmethod

from ...models import Email


class EmailAlgorithmGenerator(ABC):
    @abstractmethod
    def generate(self) -> Email:
        ...
