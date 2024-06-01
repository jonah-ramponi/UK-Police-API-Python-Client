from dateutil import parser
from datetime import datetime
from typing import Union

court_outcomes = {
    "awaiting-court-result": "Awaiting court outcome",
    "court-result-unavailable": "Court result unavailable",
    "unable-to-proceed": "Court case unable to proceed",
    "local-resolution": "Local resolution",
    "no-further-action": "Investigation complete; no suspect identified",
    "deprived-of-property": "Offender deprived of property",
    "fined": "Offender fined",
    "absolute-discharge": "Offender given absolute discharge",
    "cautioned": "Offender given a caution",
    "drugs-possession-warning": "Offender given a drugs possession warning",
    "penalty-notice-issued": "Offender given a penalty notice",
    "community-penalty": "Offender given community sentence",
    "conditional-discharge": "Offender given conditional discharge",
    "suspended-sentence": "Offender given suspended prison sentence",
    "imprisoned": "Offender sent to prison",
    "other-court-disposal": "Offender otherwise dealt with",
    "compensation": "Offender ordered to pay compensation",
    "sentenced-in-another-case": "Suspect charged as part of another case",
    "charged": "Suspect charged",
    "not-guilty": "Defendant found not guilty",
    "sent-to-crown-court": "Defendant sent to Crown Court",
    "unable-to-prosecute": "Unable to prosecute suspect",
    "formal-action-not-in-public-interest": "Formal action is not in the public interest",
    "action-taken-by-another-organisation": "Action to be taken by another organisation",
    "further-investigation-not-in-public-interest": "Further investigation is not in the public interest",
    "further-action-not-in-public-interest": "Further action is not in the public interest",
    "under-investigation": "Under investigation",
    "status-update-unavailable": "Status update unavailable",
}


def format_date(date_input: Union[str, datetime]) -> datetime:
    """
    Format date input (string or datetime object) into a string, of form "YYYY-MM".

    Args:
        date_input (str or datetime): Date input in any format.

    Returns:
        string: "YYYY-MM"
    """
    if isinstance(date_input, datetime):
        return date_input.strftime("%Y-%m")
    elif isinstance(date_input, str):
        parsed_date = parser.parse(date_input)
        return parsed_date.strftime("%Y-%m")
    else:
        raise ValueError("Invalid date input. Must be a string or datetime object.")
