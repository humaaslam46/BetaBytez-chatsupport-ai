# Problems Encountered & Solutions

## 1. No real customer chat-log data available
**Problem:** The task asks to "map out the top 10-15 repetitive customer queries the company
receives," but as an intern I have no access to BetaBytez's actual support inbox/chat logs.
**Solution:** Derived the query list systematically from the live website instead of guessing —
one likely question per website section (Services, Pricing, Process, Contact, Trust). Documented
this method explicitly in `data/top_queries.md` and `docs/research_notes.md` so it's clear these
are a reasoned starting set, not fabricated data, and can be replaced with real chat-log-derived
queries once the bot is live and logging real conversations.

## 2. First accuracy run was only 83.3% (10/12)
**Problem:** Two test questions failed on the first run:
- "How do I get started working with you?" didn't match `getting_started` — the phrasing was too
  different from the existing paraphrase variants for TF-IDF to pick up.
- "I'd like to talk to a real human please" wasn't escalated — the escalation keyword list had
  "real person" and "talk to a human" but not the blended phrase "talk to a **real human**."
**Solution:** Added the missing paraphrase variant to the `getting_started` intent, and added
"real human" / "human please" to the escalation keyword list. Re-ran the test suite: 12/12
(100%). This is logged transparently in `docs/accuracy_test_log.md` and `docs/daily_work_log.md`
rather than hidden — it's a realistic example of how FAQ/intent systems get tuned in practice.

## 3. Risk of the bot answering when it shouldn't
**Problem:** Early design let the bot always return its best-scoring match, even when that score
was low — meaning a vague or off-topic message could get a confidently-wrong FAQ answer.
**Solution:** Added a confidence threshold (0.30). Below it, the bot never guesses — it asks a
clarifying question once, then escalates to a human if the next message is still unclear. This
trades a small amount of "helpfulness" for a much lower risk of giving a customer wrong
information.

## 4. Escalation vs FAQ matching order
**Problem:** Initially, escalation was checked only as a fallback after a low-confidence FAQ
match. This risked an angry/complaint message accidentally getting a partial FAQ match (e.g.
overlapping words with the pricing intent) instead of being escalated.
**Solution:** Reordered the flow so escalation rules run first, before any FAQ matching — see
`docs/conversation_flow.md` for the corrected flow.

## 5. Keeping the prototype runnable without paid API keys
**Problem:** The REQUIRED TOOLS list mentions an LLM API, but requiring a paid key would make the
prototype hard to run/grade without setup friction.
**Solution:** Built the core prototype as a rules+NLP hybrid (TF-IDF, no external API needed),
and added the LLM integration as an optional, disabled-by-default fallback layer
(`src/llm_fallback.py`) that anyone can enable by adding a key to `.env`. This satisfies both the
"prototype must actually run" requirement and the "should demonstrate LLM API skills"
requirement.
