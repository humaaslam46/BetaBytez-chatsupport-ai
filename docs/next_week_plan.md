# Next Week's Plan (Week 4)

## Carried over from this week
- [ ] Capture screenshots of the CLI demo and the accuracy test run for `screenshots/`
- [ ] Record the 5–10 min demo video (face visible) — intentionally left for this pass
- [ ] Build the presentation slides — intentionally left for this pass

## Planned improvements to the chatbot itself
- [ ] Expand the FAQ set beyond 15 intents once/if real chat-log data becomes available, and
      replace the researched query list with actual logged customer questions.
- [ ] Add a lightweight web UI (Flask/Streamlit) around the existing `BetaBytezBot` class so it
      can be demoed as a hosted link instead of only a CLI.
- [ ] Evaluate moving from TF-IDF to sentence embeddings (e.g. `sentence-transformers`) for
      intent matching if the FAQ set grows large enough that paraphrase coverage becomes hard to
      maintain by hand.
- [ ] If the FAQ knowledge base grows to include longer documents (full service pages, case
      studies, blog posts), introduce a proper vector DB + RAG pipeline as listed in the task's
      optional tools, rather than the current flat FAQ list.
- [ ] Add conversation memory so the bot can handle simple follow-ups ("what about the Enterprise
      one?" after asking about pricing) instead of treating every message independently.
- [ ] Add logging of real (anonymized) conversations to build a genuine "top repetitive queries"
      dataset over time, replacing the researched starting set.

## Group Leader duties
- [ ] Continue consolidating weekly teammate status updates for the Team Lead.
- [ ] Continue submitting anonymous Team Lead feedback via the weekly feedback form.
