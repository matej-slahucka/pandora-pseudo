from abc import ABC, abstractmethod

from .models import Email, GetEmailRequest


class EmailSelector(ABC):
    @abstractmethod
    def select_email(self, request: GetEmailRequest) -> Email:
        ...
