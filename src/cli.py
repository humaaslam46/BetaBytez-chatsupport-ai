"""
Interactive terminal demo for the BetaBytez support bot.

Run with:  python -m src.cli
"""
from src.chatbot import BetaBytezBot


def main():
    bot = BetaBytezBot()
    print(f"BetaBytez Support Bot: {bot.greet()}\n")

    while True:
        try:
            message = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBetaBytez Support Bot: Goodbye!")
            break

        if message.lower() in {"quit", "exit"}:
            print("BetaBytez Support Bot: Goodbye!")
            break

        response = bot.respond(message)
        tag = " [ESCALATED]" if response.escalated else ""
        print(f"BetaBytez Support Bot{tag}: {response.text}\n")


if __name__ == "__main__":
    main()
