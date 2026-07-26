"""
NLP intent matcher.

Uses TF-IDF vectorization + cosine similarity to match a free-text user message
against the FAQ variants defined in faq_data.py. This is the "NLP" half of the
rules+NLP hybrid required by the task brief.
"""
from dataclasses import dataclass

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.faq_data import FAQS

DEFAULT_CONFIDENCE_THRESHOLD = 0.30


@dataclass
class MatchResult:
    intent: str | None
    answer: str | None
    score: float
    matched_variant: str | None


class IntentMatcher:
    def __init__(self, faqs=None, threshold: float = DEFAULT_CONFIDENCE_THRESHOLD):
        self.faqs = faqs if faqs is not None else FAQS
        self.threshold = threshold

        # Flatten every (intent, variant) pair so each paraphrase is its own
        # training example — this gives the vectorizer more surface area to match.
        self._corpus: list[str] = []
        self._corpus_intents: list[str] = []
        self._corpus_answers: list[str] = []
        for faq in self.faqs:
            for variant in faq["variants"]:
                self._corpus.append(variant)
                self._corpus_intents.append(faq["intent"])
                self._corpus_answers.append(faq["answer"])

        self._vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
        self._matrix = self._vectorizer.fit_transform(self._corpus)

    def match(self, message: str) -> MatchResult:
        cleaned = message.strip().lower()
        if not cleaned:
            return MatchResult(None, None, 0.0, None)

        query_vec = self._vectorizer.transform([cleaned])
        sims = cosine_similarity(query_vec, self._matrix)[0]

        best_idx = sims.argmax()
        best_score = float(sims[best_idx])

        if best_score < self.threshold:
            return MatchResult(None, None, best_score, None)

        return MatchResult(
            intent=self._corpus_intents[best_idx],
            answer=self._corpus_answers[best_idx],
            score=best_score,
            matched_variant=self._corpus[best_idx],
        )
