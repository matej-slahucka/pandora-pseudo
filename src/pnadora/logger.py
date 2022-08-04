from abc import ABC, abstractmethod

Context = str | dict | str | int | list


class Logger(ABC):
    @abstractmethod
    def debug(self, message: str, **context: Context) -> None:
        ...

    @abstractmethod
    def info(self, message: str, **context: Context) -> None:
        ...

    @abstractmethod
    def warn(self, message: str, **context: Context) -> None:
        ...

    @abstractmethod
    def error(self, message: str, **context: Context) -> None:
        ...
