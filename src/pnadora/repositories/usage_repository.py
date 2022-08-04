from abc import ABC, abstractmethod

class UsageRepository(ABC):
  def __init__(self) -> None:
    ...

  def get_usage(self) -> None:
    ...