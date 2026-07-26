# Top 15 Repetitive Customer Queries — BetaBytez

Source: facts pulled directly from the live site [betabytez.com](https://www.betabytez.com)
(Services, Pricing / Project Models, Leadership, Contact sections), July 2026.

Since BetaBytez does not have a public support ticket archive available to an intern, these
queries were compiled the way a first-line support FAQ set normally is: by mapping every distinct
question a visitor could reasonably ask against each section of the website (Services, Pricing,
Process, Contact, Trust/Security) — i.e. "what would a new visitor ask before they message
sales?" This is the standard method for bootstrapping an FAQ bot before real chat-log data exists.

| # | Intent ID | Sample query (as a customer might type it) | Category |
|---|-----------|----------------------------------------------|----------|
| 1 | `services_overview` | "What services do you offer?" | Services |
| 2 | `ai_systems` | "Do you build AI chatbots / RAG pipelines?" | Services |
| 3 | `web_dev` | "Can you build me a website in Next.js?" | Services |
| 4 | `cloud_hosting` | "Do you handle AWS/Azure deployment?" | Services |
| 5 | `data_engineering` | "Do you do data pipelines / predictive analytics?" | Services |
| 6 | `security_audit` | "Do you offer security audits or smart contract audits?" | Services |
| 7 | `pricing` | "How much does a project cost?" | Pricing |
| 8 | `pricing_startup_vs_enterprise` | "What's the difference between the Startup and Enterprise plan?" | Pricing |
| 9 | `retainer` | "Do you offer ongoing monthly support?" | Pricing |
| 10 | `timeline` | "How long does a typical project take?" | Process |
| 11 | `getting_started` | "How do I start a project with you?" | Process |
| 12 | `location` | "Where is BetaBytez based?" | Company |
| 13 | `contact_channels` | "How can I reach your team? Do you have WhatsApp?" | Company |
| 14 | `portfolio` | "Can I see examples of past work?" | Trust |
| 15 | `nda_confidentiality` | "Will you sign an NDA for our project?" | Trust |

Two additional **non-FAQ intents** are handled by the escalation layer rather than the FAQ layer
(they are queries but they should never get an automated FAQ answer):

| # | Intent ID | Sample query | Handling |
|---|-----------|---------------|----------|
| 16 | `escalate_human` | "I want to talk to a real person" | Immediate human handoff |
| 17 | `complaint` | "My project is late and nobody is replying, I want a refund" | Immediate human handoff, flagged priority |

## Source facts used to write the FAQ answers

- **Services:** AI Systems (custom LLM training & RAG pipelines), Cloud Architecture (serverless
  on AWS/Azure), Data Engineering (real-time ETL, predictive analytics), Web Engineering
  (Next.js), Motion Branding (video/3D), Audit & Security (penetration testing, smart contract
  auditing).
- **Pricing / Project Models:** Startup ($2.5k+ — MVP development, basic AI integration, cloud
  deployment), Enterprise ($10k+ — full ecosystem build, custom neural networks, 24/7 dedicated
  support), Retainer ($5k/mo — continuous scaling, technical advisory, security maintenance).
- **Leadership:** CEO Huma Aslam.
- **Location:** Lahore, Pakistan — International Hub.
- **Contact:** WhatsApp, LinkedIn, Instagram, YouTube (links on site); "Send Inquiry" contact
  form.
