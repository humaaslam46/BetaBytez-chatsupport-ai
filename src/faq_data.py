"""
FAQ knowledge base for the BetaBytez support bot.

Each entry is one intent. `variants` are paraphrases of the same question used to
train the TF-IDF intent matcher (more variants = better recall on real phrasing).
`answer` is the exact text the bot returns when that intent wins.

Facts are sourced from https://www.betabytez.com (see data/top_queries.md).
"""

FAQS = [
    {
        "intent": "services_overview",
        "variants": [
            "what services do you offer",
            "what does betabytez do",
            "what can your company build for me",
            "tell me about your services",
            "what kind of work do you do",
        ],
        "answer": (
            "We offer six core services: AI Systems (custom LLM training & RAG pipelines), "
            "Cloud Architecture (serverless AWS/Azure infrastructure), Data Engineering "
            "(real-time ETL & predictive analytics), Web Engineering (Next.js), Motion "
            "Branding (video/3D storytelling), and Audit & Security (penetration testing, "
            "smart contract auditing). Which one are you interested in?"
        ),
    },
    {
        "intent": "ai_systems",
        "variants": [
            "do you build ai chatbots",
            "can you build a rag pipeline",
            "do you do custom llm training",
            "can you integrate ai into my product",
            "do you build ai agents",
        ],
        "answer": (
            "Yes — our AI Systems unit builds custom LLM training and RAG (retrieval-augmented "
            "generation) pipelines for private data sets, including AI agents and chatbots like "
            "this one. Want me to connect you with the team to scope your use case?"
        ),
    },
    {
        "intent": "web_dev",
        "variants": [
            "can you build me a website",
            "do you build websites in nextjs",
            "do you do web development",
            "can you build a web app for my business",
        ],
        "answer": (
            "Yes, our Web Engineering unit builds industrial-grade Next.js systems with "
            "military-grade security, built to handle production traffic reliably."
        ),
    },
    {
        "intent": "cloud_hosting",
        "variants": [
            "do you handle aws deployment",
            "can you deploy on azure",
            "do you do cloud hosting",
            "can you set up serverless infrastructure",
        ],
        "answer": (
            "Yes — our Cloud Architecture unit builds serverless, globally distributed "
            "infrastructure on AWS and Azure."
        ),
    },
    {
        "intent": "data_engineering",
        "variants": [
            "do you do data pipelines",
            "can you build an etl pipeline",
            "do you do predictive analytics",
            "can you help with data engineering",
        ],
        "answer": (
            "Yes — our Data Engineering unit builds real-time ETL pipelines and predictive "
            "analytics systems for enterprises."
        ),
    },
    {
        "intent": "security_audit",
        "variants": [
            "do you do security audits",
            "can you do a penetration test",
            "do you audit smart contracts",
            "is my app secure",
        ],
        "answer": (
            "Yes — our Audit & Security unit offers comprehensive penetration testing and "
            "smart contract auditing."
        ),
    },
    {
        "intent": "pricing",
        "variants": [
            "how much does a project cost",
            "what is your pricing",
            "what do you charge",
            "how much does it cost to build a website",
        ],
        "answer": (
            "We have three project models: Startup ($2.5k+ — MVP development, basic AI "
            "integration, cloud deployment), Enterprise ($10k+ — full ecosystem build, custom "
            "neural networks, 24/7 dedicated support), and Retainer ($5k/mo — continuous "
            "scaling, technical advisory, security maintenance). Want an exact quote for your "
            "project?"
        ),
    },
    {
        "intent": "pricing_startup_vs_enterprise",
        "variants": [
            "difference between startup and enterprise plan",
            "which pricing plan should i pick",
            "is the startup plan enough for me",
        ],
        "answer": (
            "Startup ($2.5k+) fits an MVP with basic AI integration and cloud deployment. "
            "Enterprise ($10k+) is for a full ecosystem build with custom neural networks and "
            "24/7 dedicated support. If you're not sure which fits, I can connect you with the "
            "team to scope it."
        ),
    },
    {
        "intent": "retainer",
        "variants": [
            "do you offer ongoing support",
            "do you have a monthly plan",
            "do you do continuous maintenance",
        ],
        "answer": (
            "Yes — the Retainer plan is $5k/mo and covers continuous scaling, technical "
            "advisory, and security maintenance after your initial build."
        ),
    },
    {
        "intent": "timeline",
        "variants": [
            "how long does a project take",
            "what is your turnaround time",
            "how fast can you deliver",
        ],
        "answer": (
            "Timelines depend on scope and plan — Startup/MVP builds are fastest, Enterprise "
            "full-ecosystem builds take longer. Share your project scope through our inquiry "
            "form and the team will give you a concrete timeline."
        ),
    },
    {
        "intent": "getting_started",
        "variants": [
            "how do i start a project with you",
            "how do i get a quote",
            "how do i hire you",
            "what is the process to work with you",
            "how do i get started working with you",
        ],
        "answer": (
            "You can start by sending an inquiry through the 'Send Inquiry' form on our site "
            "or messaging us on WhatsApp. Tell us your goal and rough scope and the team will "
            "follow up with a plan and quote."
        ),
    },
    {
        "intent": "location",
        "variants": [
            "where is betabytez based",
            "where are you located",
            "what country are you in",
        ],
        "answer": "We're based in Lahore, Pakistan, and work as an international hub with global clients.",
    },
    {
        "intent": "contact_channels",
        "variants": [
            "how can i contact you",
            "do you have whatsapp",
            "what is your email",
            "how do i reach your team",
        ],
        "answer": (
            "You can reach us via WhatsApp, LinkedIn, Instagram, or YouTube (links on our "
            "site), or submit the 'Send Inquiry' contact form and the team will get back to "
            "you."
        ),
    },
    {
        "intent": "portfolio",
        "variants": [
            "can i see your past work",
            "do you have case studies",
            "show me examples of your projects",
            "do you have a portfolio",
        ],
        "answer": (
            "We've delivered projects like a high-speed AI data engine, a web system handling "
            "1M+ monthly users, and MVPs delivered ahead of schedule for clients including "
            "NexaCorp, StreamLine, and FinTech OS. I can have the team send you fuller case "
            "studies if you'd like."
        ),
    },
    {
        "intent": "nda_confidentiality",
        "variants": [
            "will you sign an nda",
            "can you keep my project confidential",
            "do you handle sensitive data securely",
        ],
        "answer": (
            "Yes, we're happy to sign an NDA before discussing sensitive project details — just "
            "mention it in your inquiry and the team will send one over."
        ),
    },
]

# Phrases that should trigger an immediate human handoff instead of an FAQ answer.
ESCALATION_KEYWORDS = [
    "talk to a human",
    "talk to a person",
    "speak to a human",
    "speak to someone",
    "real person",
    "real human",
    "human agent",
    "customer service rep",
    "talk to sales",
    "speak to sales",
    "connect me with someone",
    "human please",
]

# Complaint / negative-sentiment signals — also escalate, flagged as priority.
COMPLAINT_KEYWORDS = [
    "refund",
    "cancel my project",
    "not working",
    "scam",
    "angry",
    "furious",
    "terrible",
    "unacceptable",
    "still waiting",
    "no response",
    "nobody is replying",
    "disappointed",
    "complaint",
    "worst",
]
