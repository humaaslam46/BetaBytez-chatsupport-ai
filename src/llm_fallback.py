"""
Optional LLM fallback for queries the rules+NLP layer can't confidently answer.

Disabled by default (USE_LLM_FALLBACK = False) so the prototype runs with zero
API keys and zero cost. Flip the flag and set OPENAI_API_KEY or ANTHROPIC_API_KEY
in .env to enable it.

Design choice: the LLM is given ONLY the FAQ knowledge base as context and is
instructed not to invent company facts — it should say it doesn't know rather
than hallucinate pricing, services, etc. that aren't in the source data.
"""
import os

from dotenv import load_dotenv

from src.faq_data import FAQS

load_dotenv()

USE_LLM_FALLBACK = False  # flip to True once you've added an API key to .env

SYSTEM_PROMPT = (
    "You are a first-line customer support assistant for BetaBytez, an engineering studio. "
    "Answer ONLY using the FAQ knowledge base provided below. If the answer isn't in the "
    "knowledge base, say you're not sure and offer to connect the user with the team — never "
    "invent pricing, services, or policies that aren't listed.\n\nFAQ KNOWLEDGE BASE:\n"
    + "\n".join(f"- Q: {faq['variants'][0]}\n  A: {faq['answer']}" for faq in FAQS)
)


def get_llm_fallback_response(message: str) -> str | None:
    if not USE_LLM_FALLBACK:
        return None

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if api_key:
        try:
            import anthropic

            client = anthropic.Anthropic(api_key=api_key)
            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=300,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": message}],
            )
            return response.content[0].text
        except Exception as exc:  # pragma: no cover - network/optional path
            print(f"[llm_fallback] Anthropic call failed: {exc}")
            return None

    openai_key = os.getenv("OPENAI_API_KEY")
    if openai_key:
        try:
            from openai import OpenAI

            client = OpenAI(api_key=openai_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": message},
                ],
                max_tokens=300,
            )
            return response.choices[0].message.content
        except Exception as exc:  # pragma: no cover - network/optional path
            print(f"[llm_fallback] OpenAI call failed: {exc}")
            return None

    return None
