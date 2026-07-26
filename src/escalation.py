"""
Rule-based escalation-to-human logic.

Runs BEFORE intent matching. If a message contains an explicit human-handoff
phrase or a complaint/negative-sentiment signal, the bot skips the FAQ layer
entirely and routes straight to a human-handoff response.
"""
from src.faq_data import COMPLAINT_KEYWORDS, ESCALATION_KEYWORDS

HUMAN_HANDOFF_MESSAGE = (
    "Got it — I'll connect you with a member of the BetaBytez team who can help further. "
    "Someone will follow up shortly. In the meantime, is there anything else I can try to "
    "answer?"
)

PRIORITY_HANDOFF_MESSAGE = (
    "I'm sorry to hear that — I'm flagging this for a team member to follow up with you "
    "as a priority. Could you share a couple more details (e.g. your project name / order "
    "reference) so they can look into it right away?"
)


def check_escalation(message: str) -> tuple[bool, str | None, str | None]:
    """
    Returns (should_escalate, reason, response_message).
    reason is one of: "explicit_request", "complaint", or None.
    """
    cleaned = message.strip().lower()

    for phrase in ESCALATION_KEYWORDS:
        if phrase in cleaned:
            return True, "explicit_request", HUMAN_HANDOFF_MESSAGE

    for phrase in COMPLAINT_KEYWORDS:
        if phrase in cleaned:
            return True, "complaint", PRIORITY_HANDOFF_MESSAGE

    return False, None, None
