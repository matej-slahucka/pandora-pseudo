from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Protocol


class Tier(str, Enum):
    TIER1 = "tier1"
    TIER2 = "tier2"
    TIER3 = "tier3"


class Algorithm(str, Enum):
    BID = "BID"
    NAME_SURNAME_NUM = "NAME_SURNAME_NUM"
    SHORTENED_NAME = "SHORTENED_NAME"


@dataclass
class Email:
    domain: str
    name: str


@dataclass
class Domain:
    domain: str


# can be expanded with login
Resource = Email | Domain


class Rule(Protocol):
    id: int
    frequency_window: int  # number of days
    frequency: int
    name: str


class AlgorithmData(Protocol):
    name: str
    surname: str
    number: int


Channel = str
Carrier = str


@dataclass
class GetEmailRequestBase:
    tier: Tier
    candidates: list[Email]
    channel: Channel
    carrier: Carrier
    booking_id: int


class GetEmailRequestEmail(GetEmailRequestBase):
    pass


@dataclass
class GetEmailRequestDomain(GetEmailRequestBase):
    algorithm_data: AlgorithmData
    algorithm: Algorithm


GetEmailRequest = GetEmailRequestEmail | GetEmailRequestDomain


class StoredEmail(Protocol):
    id: int
    email: Email
    tld: str
    tier: Tier
    active: bool
    created: datetime
    updated: datetime


@dataclass
class ResourceWithUsage:
    resource: Resource
    frequency: int
