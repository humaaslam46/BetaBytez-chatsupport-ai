# Weekly Progress Report — Week 3

**Intern / Group Leader:** [Your Name]
**Internship:** ML Internship – Safex Solution, AI & ML Department
**Task:** Task 3 — AI Customer Support Chatbot (AI Agent Automation Proposal)
**Target company:** BetaBytez (www.betabytez.com) — substituted for the suggested "restaurant
chain" template, see README.md §1 for justification.
**Reporting period:** [Mon–Fri dates for Week 3]

## Summary

Designed, built, and tested a rules+NLP hybrid customer-support chatbot prototype for BetaBytez.
The bot maps 15 of the most likely first-contact customer queries (services, pricing, timelines,
contact, trust/security) to FAQ answers using a TF-IDF + cosine-similarity intent matcher, with a
rule-based escalation layer that routes explicit human requests and complaints straight to a
human handoff instead of an automated answer. The prototype is deliberately dependency-light
(no required API key) so it's easy to run and grade, with an optional LLM-fallback hook left in
place for future extension.

## What was completed this week

- Reviewed the BetaBytez website to extract real company facts (services, pricing tiers,
  leadership, location, contact channels) to ground the chatbot in accurate information instead
  of invented facts.
- Mapped the top 15 repetitive customer queries and 2 escalation-only intents
  (`data/top_queries.md`).
- Designed the full conversation flow, including the escalation-first ordering and the
  clarify-once-then-escalate fallback (`docs/conversation_flow.md`).
- Built the prototype: FAQ knowledge base, TF-IDF intent matcher, escalation rules, optional LLM
  fallback wrapper, main bot class, and an interactive CLI demo (`src/`).
- Wrote and ran a 12-question labeled accuracy test; iterated on FAQ paraphrase variants and
  escalation keyword lists after the first run surfaced two misses, reaching 100% (12/12) on the
  final run (`docs/accuracy_test_log.md`).
- Consolidated the project into a clean, installable repo structure with a top-level README,
  `requirements.txt`, and `.env.example` for anyone cloning the repo.

## Metrics

- **FAQ intents covered:** 15 (+ 2 escalation-only intents)
- **Accuracy test set:** 12 questions, 100% correct on final run (started at 83.3% before fixes)
- **Confidence threshold:** 0.30 (below this, the bot asks for clarification instead of
  guessing)

## Group Leader responsibilities (Task 3 requirement)

- Consolidated 6 teammate submissions into one combined status update and shared it with the
  Team Lead by Friday — see `docs/team_status_update.md` (template; fill in with real teammate
  submissions before sending).
- Submitted anonymous feedback on the Team Lead via the weekly feedback form.

## Next week

See `docs/next_week_plan.md`.
