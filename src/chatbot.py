"""
BetaBytezBot — the main conversation engine.

Flow per message:
  1. Escalation rules (explicit human request / complaint) — highest priority.
  2. NLP intent match against the FAQ knowledge base.
  3. Optional LLM fallback (disabled by default).
  4. Clarification / graceful "I don't know, want a human?" fallback.

See docs/conversation_flow.md for the visual diagram of this logic.
"""
from dataclasses import dataclass

from src.escalation import check_escalation
from src.intent_matcher import IntentMatcher
from src.llm_fallback import get_llm_fallback_response

GREETING = (
    "Hi! I'm the BetaBytez support assistant. Ask me about our services, pricing, "
    "timelines, or how to start a project. Type 'human' any time to reach a real "
    "person, or 'quit' to exit."
)

CLARIFY_MESSAGE = (
    "I'm not fully sure I understood that — could you rephrase, or tell me if it's about "
    "services, pricing, timelines, or getting started? I can also connect you with the "
    "team if you'd rather ask a human."
)

FALLBACK_ESCALATE_MESSAGE = (
    "I don't have a confident answer for that one. I'll connect you with a member of the "
    "BetaBytez team who can help — they'll follow up shortly."
)


@dataclass
class BotResponse:
    text: str
    matched_intent: str | None
    confidence: float
    escalated: bool
    escalation_reason: str | None


class BetaBytezBot:
    def __init__(self, confidence_threshold: float = 0.30):
        self.matcher = IntentMatcher(threshold=confidence_threshold)
        self._awaiting_clarification = False

    def greet(self) -> str:
        return GREETING

    def respond(self, message: str) -> BotResponse:
        # 1. Escalation rules take priority over everything else.
        should_escalate, reason, escalation_text = check_escalation(message)
        if should_escalate:
            return BotResponse(
                text=escalation_text,
                matched_intent=None,
                confidence=1.0,
                escalated=True,
                escalation_reason=reason,
            )

        # 2. NLP intent match.
        result = self.matcher.match(message)
        if result.intent is not None:
            self._awaiting_clarification = False
            return BotResponse(
                text=result.answer,
                matched_intent=result.intent,
                confidence=result.score,
                escalated=False,
                escalation_reason=None,
            )

        # 3. Optional LLM fallback (no-op unless enabled in src/llm_fallback.py).
        llm_answer = get_llm_fallback_response(message)
        if llm_answer:
            return BotResponse(
                text=llm_answer,
                matched_intent="llm_fallback",
                confidence=result.score,
                escalated=False,
                escalation_reason=None,
            )

        # 4. Ask once for clarification, then escalate on repeated low confidence.
        if not self._awaiting_clarification:
            self._awaiting_clarification = True
            return BotResponse(
                text=CLARIFY_MESSAGE,
                matched_intent=None,
                confidence=result.score,
                escalated=False,
                escalation_reason=None,
            )

        self._awaiting_clarification = False
        return BotResponse(
            text=FALLBACK_ESCALATE_MESSAGE,
            matched_intent=None,
            confidence=result.score,
            escalated=True,
            escalation_reason="low_confidence_repeated",
        )
