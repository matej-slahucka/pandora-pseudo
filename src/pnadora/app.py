from __future__ import annotations

from .email_address_getter import EmailAddressGetter
from .email_selector import EmailSelector
from .models import Email, GetEmailRequest, Tier
from .repositories import AccountRuleRepository, DomainRuleRepository, RuleRepository
from .rule_evaluator import RuleEvaluator
from .usage_checker import UsageCheckerFactory


class RuleRepositoryFactory:
    TIER_TO_RULE_REPOSITORY = {
        Tier.TIER1: DomainRuleRepository,
        Tier.TIER2: DomainRuleRepository,
        Tier.TIER3: AccountRuleRepository,
    }

    def create_rule_repository(self, tier: Tier) -> RuleRepository:
        return self.TIER_TO_RULE_REPOSITORY[tier]()


class GetEmailAddressError(Exception):
    pass


class EmailSelectorFactory:
    def create_email_selector(self) -> EmailSelector:
        raise NotImplemented


def get_email_address_use_case(
    request: GetEmailRequest,
    rule_repository_factory: RuleRepositoryFactory,
    usage_checker_factory: UsageCheckerFactory,
    email_selector_factory: EmailSelectorFactory,
) -> Email:
    rule_repository = rule_repository_factory.create_rule_repository(request.tier)

    rule_evaluator = RuleEvaluator(rule_repository)
    usage_checker = usage_checker_factory.create_usage_checker(request.tier)
    email_selector = email_selector_factory.create_email_selector()

    email_address_getter = EmailAddressGetter(
        rule_evaluator, usage_checker, email_selector
    )

    email = email_address_getter.get_email_address(request)

    if email is None:
        raise GetEmailAddressError

    return email
