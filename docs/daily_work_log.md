# Daily Work Log — Task 3 (Week 3)

Fill in real dates/hours as you actually do the work — the structure below reflects the order
the project was actually built in during prototyping.

## Day 1 — Research & Scoping
- Read the task brief and decided on the company substitution (BetaBytez, noted in README).
- Reviewed www.betabytez.com end-to-end: services, pricing/project models, leadership, contact
  channels.
- Drafted the top 10–15 repetitive customer queries by mapping one likely question per website
  section (`data/top_queries.md`).
- **Hours:** [x]

## Day 2 — Conversation Flow Design
- Designed the conversation flow: escalation-first ordering, FAQ intent matching, confidence
  threshold, clarify-once-then-escalate fallback, optional LLM fallback slot.
- Documented it as a Mermaid diagram (`docs/conversation_flow.md`).
- **Hours:** [x]

## Day 3 — Prototype Build (Part 1)
- Built the FAQ knowledge base with paraphrase variants (`src/faq_data.py`).
- Built the TF-IDF + cosine-similarity intent matcher (`src/intent_matcher.py`).
- Built the rule-based escalation checker (`src/escalation.py`).
- **Hours:** [x]

## Day 4 — Prototype Build (Part 2) + Testing
- Built the main `BetaBytezBot` conversation engine and CLI demo (`src/chatbot.py`, `src/cli.py`).
- Wrote 12 labeled sample questions and the accuracy test harness (`tests/`).
- First test run: 10/12 (83.3%). Debugged two misses — a paraphrase gap on the
  "getting started" intent and a missed escalation phrase ("talk to a **real** human"). Fixed
  both and re-ran to 12/12 (100%).
- **Hours:** [x]

## Day 5 — Documentation, Optional LLM Hook, Group Leader Duties
- Wrote the optional constrained LLM fallback wrapper (`src/llm_fallback.py`), disabled by
  default.
- Wrote README, weekly progress report, research notes, problems & solutions, next week's plan.
- Consolidated teammate submissions into one status update for the Team Lead
  (`docs/team_status_update.md`) and submitted anonymous Team Lead feedback via the weekly form.
- **Hours:** [x]

---
**Total hours this week:** [x]
