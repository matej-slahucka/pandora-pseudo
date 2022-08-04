from __future__ import annotations

from .email_address_getter import EmailAddressGetter
from .email_selector import EmailSelector
from .models import Email, GetEmailRequest, Tier
from .rule_evaluator import RuleEvaluator
from .usage_checker import UsageChecker


class RuleRepositoryFactory:
    TIER_TO_RULE_REPOSITORY = {
        Tier.TIER1: None,
        Tier.TIER2: DomainRuleRepository,
        Tier.TIER3: AccountRuleRepository,
    }

    def create_rule_repository(self, tier: Tier) -> RuleEvaluator:
        return self.TIER_TO_RULE_REPOSITORY[tier]


def get_email_address_use_case(
    request: GetEmailRequest,
    rule_repository_factory: RuleRepositoryFactory,
    usage_repository_factory: UsageRepositoryFactory,
) -> Email:
    rule_repository = rule_repository_factory.create_rule_repository(request.tier)
    usage_repository = usage_repository_factory.create_usage_repository(request.tier)

    rule_evaluator = RuleEvaluator(rule_repository)
    usage_checker = UsageChecker(usage_repository)
    email_selector: EmailSelector  # TODO from email_selector_factory

    email_address_getter = EmailAddressGetter(
        rule_evaluator, usage_checker, email_selector
    )

    return email_address_getter.get_email_address(request)
