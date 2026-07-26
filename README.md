# BetaBytez AI Customer Support Chatbot

**Internship:** ML Internship – Safex Solution
**Project:** AI & ML Department – AI Agent Automation Proposal – Task 3
**Author:** Group Leader (Team submission)
**Week:** 3

---

## 1. Company & Substitution Note

The task template asks us to build the chatbot for a *chain of restaurants*, with an option to
substitute a real company in the **same space** (i.e. a business that handles a high volume of
repetitive, first-line customer queries).

**Substitution used:** [BetaBytez](https://www.betabytez.com) — a real engineering studio
(Lahore, Pakistan) offering AI Systems, Cloud Architecture, Data Engineering, Web Engineering,
Motion Branding, and Audit & Security services, with three published pricing tiers (Startup,
Enterprise, Retainer).

**Why this substitution is valid:** Like a restaurant chain, BetaBytez's website receives a high
volume of near-identical first-contact questions from visitors (services, pricing, timelines,
tech stack, how to start a project, contact info, etc.). These are exactly the kind of
repetitive, low-complexity, high-volume queries that a first-line support chatbot is meant to
automate, with a clear escalation path to a human for sales conversations, complaints, or
anything outside the FAQ scope. All company-specific facts used in this project (services,
pricing tiers, contact channels, location) were taken directly from the live BetaBytez website
and are documented in [`data/top_queries.md`](data/top_queries.md).

---

## 2. What's in this repo

```
betabytez-support-chatbot/
├── README.md                       <- you are here
├── requirements.txt
├── .env.example
├── src/
│   ├── faq_data.py                 <- 15 mapped FAQ intents (the knowledge base)
│   ├── intent_matcher.py           <- TF-IDF + cosine similarity NLP matcher
│   ├── escalation.py               <- rule-based escalation-to-human triggers
│   ├── llm_fallback.py             <- optional LLM API fallback (OpenAI/Anthropic)
│   ├── chatbot.py                  <- main BetaBytezBot class (conversation engine)
│   └── cli.py                      <- interactive terminal demo
├── data/
│   └── top_queries.md              <- top 15 repetitive queries, mapped to intents
├── tests/
│   ├── sample_questions.json       <- 12 labeled test questions
│   └── test_accuracy.py            <- runs the test set, prints/saves accuracy log
├── docs/
│   ├── conversation_flow.md        <- Mermaid conversation-flow diagram
│   ├── accuracy_test_log.md        <- generated test results (deliverable)
│   ├── weekly_progress_report.md   <- Week 3 progress report
│   ├── daily_work_log.md           <- day-by-day work log
│   ├── research_notes.md           <- research / working notes
│   ├── problems_encountered.md     <- problems & solutions
│   ├── next_week_plan.md           <- plan for Week 4
│   └── team_status_update.md       <- Group Leader's consolidated team status update
├── webapp/                         <- branded browser chat UI (Flask)
│   ├── app.py                      <- REST API wrapping the same BetaBytezBot engine
│   ├── templates/index.html
│   └── static/{style.css, script.js, logo.png}
└── screenshots/
    └── README.md                   <- placeholder / instructions for adding screenshots
```

## 3. How it works (architecture)

This is a **rules + NLP hybrid** chatbot (as allowed by the task's "REQUIRED TOOLS" list), not a
pure LLM wrapper, so it runs **fully offline with zero API keys** out of the box:

1. **Input normalization** — lowercase, strip punctuation.
2. **Escalation rules first** (`src/escalation.py`) — checks for explicit human-handoff phrases
   ("talk to a human", "speak to sales") and negative/complaint sentiment keywords ("refund",
   "angry", "not working", "scam"). If matched, the bot immediately routes to a human-handoff
   message instead of trying to answer.
3. **Intent matching** (`src/intent_matcher.py`) — TF-IDF vectorizes the user message and the 15
   FAQ questions (+ paraphrase variants), then uses cosine similarity to find the best-matching
   intent. This is the "NLP" half of the hybrid.
4. **Confidence threshold** — if the best match's similarity score is below a threshold, the bot
   does **not** guess; it either asks a clarifying question once, or escalates.
5. **Optional LLM fallback** (`src/llm_fallback.py`) — if an `OPENAI_API_KEY` or
   `ANTHROPIC_API_KEY` is present in `.env`, unmatched queries can optionally be passed to an LLM
   (constrained to only answer using the FAQ knowledge base as context — no hallucinated company
   facts) before falling back to human escalation. This is disabled by default so the prototype
   is runnable and gradeable with no paid API required.

See [`docs/conversation_flow.md`](docs/conversation_flow.md) for the full flow diagram.

## 4. Setup

```bash
git clone <this-repo-url>
cd betabytez-support-chatbot
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # optional — only needed for LLM fallback mode
```

## 5. Run the demo

```bash
python -m src.cli
```

Example session:

```
BetaBytez Support Bot: Hi! I'm the BetaBytez support assistant. Ask me about our
services, pricing, timelines, or how to start a project. Type 'human' any time to
reach a real person, or 'quit' to exit.

You: how much does a website cost
BetaBytez Support Bot: Our project models are: Startup ($2.5k+, MVP + basic AI +
cloud deployment), Enterprise ($10k+, full ecosystem build + custom neural
networks + 24/7 support), and Retainer ($5k/mo, continuous scaling + technical
advisory). A Next.js website typically falls under Startup or Enterprise
depending on scope. Want me to connect you with the team for an exact quote?
```

## 5b. Run the browser chat UI (recommended for demos/screenshots/video)

The CLI in section 5 is useful for quick testing, but `webapp/` wraps the exact same
`BetaBytezBot` engine in a small Flask app with a branded chat interface — this is what you'd
actually screen-record for the demo video or screenshot for the deliverables.

```bash
python -m webapp.app
```

Then open **http://127.0.0.1:5000** in your browser. You'll get:

- A branded chat window (BetaBytez logo, colors, "crafting digital magic" tagline)
- Clickable suggested-question chips for the most common intents
- Live typing indicator while the bot "thinks"
- A visible badge on each bot reply showing which intent matched and its confidence score, or
  an "escalated to human" flag when the escalation layer fires — useful for showing graders
  *why* the bot responded the way it did
- A "Reset conversation" button to start a fresh session

No chatbot logic lives in `webapp/app.py` — it only handles HTTP and per-browser-session state.
The actual conversation engine is still the same `src/chatbot.py` used by the CLI, so both
interfaces stay in sync automatically.

## 6. Run the accuracy test

```bash
python -m tests.test_accuracy
```

This runs the 12 labeled sample questions in `tests/sample_questions.json` through the bot,
compares the predicted intent to the expected intent, prints a per-question pass/fail table, and
writes the results to `docs/accuracy_test_log.md`.

## 7. Known limitations / next steps

See [`docs/problems_encountered.md`](docs/problems_encountered.md) and
[`docs/next_week_plan.md`](docs/next_week_plan.md).

## 8. Deliverables checklist (per task brief)

- [x] Top 10–15 repetitive customer queries mapped → `data/top_queries.md`
- [x] Conversation-flow diagram (FAQ + escalation) → `docs/conversation_flow.md`
- [x] Working prototype (rules + NLP hybrid, LLM-fallback optional) → `src/`
- [x] Tested with 10+ sample questions, accuracy recorded → `tests/`, `docs/accuracy_test_log.md`
- [x] Company substitution documented → this file, section 1
- [x] Weekly Progress Report, Daily Work Log, Research Notes, Problems & Solutions, Next Week's
      Plan → `docs/`
- [x] Group Leader consolidated team status update template → `docs/team_status_update.md`
- [ ] Screenshots/evidence → add to `screenshots/` (placeholder included)
- [ ] Demo video, presentation slides → intentionally left for a later pass
