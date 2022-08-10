class EmailSelectorError(Exception):
    pass


class RuleNotFoundError(EmailSelectorError):
    pass


class UnexpectedRequestError(EmailSelectorError):
    pass


class UnexpectedResourceError(EmailSelectorError):
    pass
