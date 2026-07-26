# Conversation Flow Diagram — BetaBytez Support Bot

This diagram renders natively on GitHub (Mermaid). It matches the logic implemented in
`src/chatbot.py`.

```mermaid
flowchart TD
    A([User sends a message]) --> B{Escalation rules check<br/>src/escalation.py}

    B -->|Explicit human request<br/>e.g. "talk to a human"| C[Human handoff message<br/>+ flag conversation for a team member]
    B -->|Complaint / negative sentiment<br/>e.g. "refund", "not working"| D[Priority human handoff message<br/>+ ask for order/project reference<br/>+ flag as priority]
    B -->|Neither| E{NLP intent match<br/>TF-IDF + cosine similarity<br/>src/intent_matcher.py}

    E -->|Confidence >= 0.30| F[Return matched FAQ answer<br/>15 intents: services, pricing,<br/>timeline, contact, etc.]
    E -->|Confidence < 0.30| G{LLM fallback enabled?<br/>src/llm_fallback.py}

    G -->|Yes, key configured| H[LLM answers using ONLY<br/>the FAQ knowledge base as context]
    G -->|No / not configured| I{First low-confidence<br/>message in this turn?}

    I -->|Yes| J[Ask one clarifying question:<br/>rephrase, or pick a topic]
    I -->|No - already asked once| K[Escalate to human<br/>"I don't have a confident<br/>answer, connecting you now"]

    C --> Z([End turn / await next message])
    D --> Z
    F --> Z
    H --> Z
    J --> Z
    K --> Z
```

## Design notes

- **Escalation checks run first, before any FAQ matching.** This guarantees a customer who is
  angry or explicitly asking for a human is never met with an automated FAQ answer that would
  feel dismissive.
- **Complaints are escalated with priority flagging** and the bot asks for a reference so the
  human agent can act immediately, rather than making the customer repeat themselves.
- **Confidence threshold (0.30)** was chosen empirically — see
  [`accuracy_test_log.md`](accuracy_test_log.md) for the test results that validated it. Below
  this threshold the bot refuses to guess, because a wrong FAQ answer is worse than asking for
  clarification.
- **Clarify-once-then-escalate**: the bot never loops a confused customer more than once — if a
  second low-confidence message comes in, it escalates automatically rather than frustrating the
  user with repeated "I don't understand" replies.
- **LLM fallback is optional and constrained**: if enabled, the LLM is given the FAQ knowledge
  base as its only source of truth and is explicitly instructed not to invent company facts
  (pricing, services, policies) that aren't in that knowledge base.
