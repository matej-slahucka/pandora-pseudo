from enum import Enum
from typing import Protocol

class Tier(str, Enum):
  TIER1 = "tier1"
  TIER2 = "tier2"
  TIER3 = "tier3"


class Email(Protocol):
  domain: str
  name: str


class Rule(Protocol):
  ...


class GetEmailRequest(Protocol):
  tier: Tier
  candidate: Email
  channel: str
  carrier: str