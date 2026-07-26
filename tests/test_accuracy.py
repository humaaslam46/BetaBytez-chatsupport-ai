"""
Runs the labeled sample questions in tests/sample_questions.json through the bot,
compares predicted vs expected intent, prints a pass/fail table, and writes the
results to docs/accuracy_test_log.md (a required deliverable).

Run with:  python -m tests.test_accuracy
"""
import json
import os
from datetime import datetime

from src.chatbot import BetaBytezBot

SAMPLE_PATH = os.path.join(os.path.dirname(__file__), "sample_questions.json")
LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "docs", "accuracy_test_log.md")


def run_tests():
    with open(SAMPLE_PATH, "r", encoding="utf-8") as f:
        samples = json.load(f)

    rows = []
    correct = 0

    for sample in samples:
        # Fresh bot per question so the "ask-once-then-escalate" clarification
        # state from one test question doesn't leak into the next.
        bot = BetaBytezBot()
        response = bot.respond(sample["question"])

        predicted = "ESCALATE" if response.escalated else response.matched_intent
        is_correct = predicted == sample["expected_intent"]
        correct += int(is_correct)

        rows.append(
            {
                "question": sample["question"],
                "expected": sample["expected_intent"],
                "predicted": predicted,
                "confidence": round(response.confidence, 3),
                "correct": is_correct,
                "response_text": response.text,
            }
        )

    accuracy = correct / len(samples) if samples else 0.0
    return rows, accuracy


def write_log(rows, accuracy):
    lines = [
        "# Accuracy Test Log — BetaBytez Support Bot",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        f"**Result: {sum(r['correct'] for r in rows)}/{len(rows)} correct "
        f"({accuracy * 100:.1f}% accuracy)**",
        "",
        "| # | Question | Expected | Predicted | Confidence | Pass? |",
        "|---|----------|----------|-----------|------------|-------|",
    ]

    for i, row in enumerate(rows, start=1):
        mark = "✅" if row["correct"] else "❌"
        lines.append(
            f"| {i} | {row['question']} | `{row['expected']}` | `{row['predicted']}` | "
            f"{row['confidence']} | {mark} |"
        )

    lines.append("")
    lines.append("## Full bot responses")
    lines.append("")
    for i, row in enumerate(rows, start=1):
        lines.append(f"**{i}. {row['question']}**")
        lines.append(f"> {row['response_text']}")
        lines.append("")

    with open(LOG_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    rows, accuracy = run_tests()

    print(f"\nAccuracy: {sum(r['correct'] for r in rows)}/{len(rows)} "
          f"({accuracy * 100:.1f}%)\n")
    for i, row in enumerate(rows, start=1):
        mark = "PASS" if row["correct"] else "FAIL"
        print(f"[{mark}] Q{i}: {row['question']!r} -> expected={row['expected']} "
              f"predicted={row['predicted']} (conf={row['confidence']})")

    write_log(rows, accuracy)
    print(f"\nLog written to {os.path.abspath(LOG_PATH)}")


if __name__ == "__main__":
    main()
