"""
Flask web app for the BetaBytez support bot.

Wraps the existing src.chatbot.BetaBytezBot in a small REST API + serves a
branded chat UI. No chatbot logic lives here — this file only handles HTTP
and per-browser-session bot instances, so src/ stays the single source of
truth for the actual conversation engine (used by both this app and the CLI).

Run with:  python -m webapp.app
Then open: http://127.0.0.1:5000
"""
import uuid

from flask import Flask, jsonify, render_template, request, session

from src.chatbot import BetaBytezBot

app = Flask(__name__)
app.secret_key = "dev-secret-key-change-if-deploying-publicly"

# In-memory session store: {session_id: BetaBytezBot}. Fine for a local
# prototype/demo; would move to a real session/DB store for production.
_bots: dict[str, BetaBytezBot] = {}


def _get_bot() -> BetaBytezBot:
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
    session_id = session["session_id"]

    if session_id not in _bots:
        _bots[session_id] = BetaBytezBot()

    return _bots[session_id]


@app.route("/")
def index():
    bot = _get_bot()
    return render_template("index.html", greeting=bot.greet())


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True) or {}
    message = (data.get("message") or "").strip()

    if not message:
        return jsonify({"error": "Empty message"}), 400

    bot = _get_bot()
    response = bot.respond(message)

    return jsonify(
        {
            "reply": response.text,
            "escalated": response.escalated,
            "matched_intent": response.matched_intent,
            "confidence": round(response.confidence, 3),
        }
    )


@app.route("/api/reset", methods=["POST"])
def reset():
    if "session_id" in session:
        _bots.pop(session["session_id"], None)
        session.pop("session_id", None)
    return jsonify({"status": "reset"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
