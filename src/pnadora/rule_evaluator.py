from .models import Email, StoredEmail
from .repositories import EmailRepository


class RuleEvaluator:
    def __init__(self, email_repository: EmailRepository) -> None:
        self._email_repository = email_repository

    def get_usable_candidates(self, candidates: list[Email]) -> list[StoredEmail]:
        stored_emailes = self._email_repository.find_emails(candidates)
        active_emails = self._filter_active_emails(stored_emailes)
        # TODO: in the current Pandora impl there is not check for rules, should it be there?
        return active_emails

    def _filter_active_emails(self, emails: list[StoredEmail]) -> list[StoredEmail]:
        return [email for email in emails if email.active]
