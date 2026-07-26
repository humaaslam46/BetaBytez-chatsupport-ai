# Research / Working Notes — Task 3

## Company research

- Source: [www.betabytez.com](https://www.betabytez.com) (live site, reviewed July 2026).
- BetaBytez is an engineering studio, not a restaurant chain — the task brief explicitly allows
  substituting a real company "in the same space," meaning: a business whose website receives a
  high volume of repetitive, low-complexity first-contact questions. BetaBytez qualifies:
  visitors reliably ask about services, pricing, timelines, and how to start a project before
  ever talking to a human.
- Facts extracted: 6 service categories (AI Systems, Cloud Architecture, Data Engineering, Web
  Engineering, Motion Branding, Audit & Security), 3 pricing tiers (Startup $2.5k+, Enterprise
  $10k+, Retainer $5k/mo), CEO Huma Aslam, HQ Lahore Pakistan, contact via WhatsApp / LinkedIn /
  Instagram / YouTube / inquiry form.
- No public support-ticket archive is available to an intern, so the "top 10-15 repetitive
  queries" were derived by systematically asking "what would a new visitor ask about this
  section?" for every section of the site (Services, Pricing, Process, Contact, Trust). This is
  a standard cold-start method for FAQ bots before real chat logs exist.

## Architecture decisions

- **Rules + NLP hybrid chosen over a pure LLM wrapper.** Task brief explicitly lists this as an
  acceptable approach, and it has real advantages for a first prototype: no API cost, fully
  reproducible test results, transparent/debuggable matching (you can see exactly why an intent
  did or didn't match), and no hallucination risk on company facts like pricing.
- **TF-IDF + cosine similarity** was chosen over pure keyword rules because customers phrase the
  same question many different ways ("how much does it cost" vs "what's your pricing" vs "how
  much for a website"). TF-IDF with bigrams captures this variation without needing a full
  embedding model or external API.
- **Escalation rules run before intent matching, not after.** Early design had escalation as a
  fallback for low-confidence matches only. Changed this after realizing an angry or explicit
  "let me talk to a human" message could accidentally partially match an FAQ (e.g. "refund" +
  "cost" language overlapping with the pricing intent) and get an FAQ answer instead of a human
  handoff — which would be a worse outcome than a wrong FAQ answer on a neutral question.
- **Confidence threshold of 0.30** was set by trial: below this, TF-IDF matches were mostly noise
  (matching on stray shared words rather than actual topic overlap); above it, matches were
  reliably on-topic in testing.
- **LLM fallback kept optional, not default.** Keeps the graded prototype runnable with zero
  setup friction and zero cost, while still demonstrating the LLM-API integration pattern the
  task's REQUIRED TOOLS section asks about. It's also explicitly constrained to answer only from
  the FAQ knowledge base, to avoid the classic support-bot failure mode of an LLM inventing
  pricing or policies that don't exist.

## Alternatives considered

- **Pure LLM (OpenAI/Anthropic) with no rules layer:** rejected for the prototype because it
  would require a paid API key to even demo/grade, and would be harder to produce a reliable,
  reproducible accuracy log from (LLM outputs vary run to run).
- **Pure keyword/regex rules with no NLP:** rejected because it's brittle to paraphrasing and
  wouldn't count as the "NLP hybrid" the brief describes.
- **Vector DB / RAG:** noted as a listed optional tool in the brief, but judged overkill for a
  15-intent FAQ set at this stage — flagged in `next_week_plan.md` as the natural next step if
  the FAQ set grows significantly or needs to ingest longer documents (e.g. full service pages,
  case studies).
