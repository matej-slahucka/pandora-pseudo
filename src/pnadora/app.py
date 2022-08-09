from __future__ import annotations

from .email_address_getter import EmailAddressGetter
from .email_selector.resource_selector import EmailSelector
from .logger import Logger
from .models import Email, GetEmailRequest, Resource, Tier
from .repositories import (
    AccountEmailRepository,
    DomainEmailRepository,
    ResourceRepository,
)
from .rule_evaluator import RuleEvaluator
from .usage_checker import UsageCheckerFactory


class EmailRepositoryFactory:
    TIER_TO_RULE_REPOSITORY = {
        Tier.TIER1: DomainEmailRepository,
        Tier.TIER2: DomainEmailRepository,
        Tier.TIER3: AccountEmailRepository,
    }

    def create_email_repository(self, _: Tier) -> ResourceRepository:
        raise NotImplemented


class GetEmailAddressError(Exception):
    pass


class EmailSelectorFactory:
    def create_email_selector(self) -> EmailSelector[Resource, GetEmailRequest]:
        raise NotImplemented


def get_email_address_use_case(
    request: GetEmailRequest,
    email_repository_factory: EmailRepositoryFactory,
    usage_checker_factory: UsageCheckerFactory,
    email_selector_factory: EmailSelectorFactory,
    logger: Logger,
) -> Email:
    rule_repository = email_repository_factory.create_email_repository(request.tier)

    rule_evaluator = RuleEvaluator(rule_repository)
    usage_checker = usage_checker_factory.create_usage_checker(request.tier)
    email_selector = email_selector_factory.create_email_selector()

    email_address_getter = EmailAddressGetter(
        rule_evaluator, usage_checker, email_selector, logger
    )

    email = email_address_getter.get_email_address(request)

    if email is None:
        raise GetEmailAddressError

    return email
