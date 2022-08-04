from datetime import datetime
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
    id: int
    frequency_window: int  # number of days
    frequency: int
    name: str


Channel = str
Carrier = str


class GetEmailRequest(Protocol):
    tier: Tier
    candidates: list[Email]
    channel: Channel
    carrier: Carrier


class StoredEmail(Protocol):
    id: int
    email: Email
    tld: str
    tier: Tier
    active: bool
    created: datetime
    updated: datetime


class EmailWithUsage(Protocol):
    email: Email
    frequency: int
