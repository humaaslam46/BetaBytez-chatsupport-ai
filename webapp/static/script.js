const messagesEl = document.getElementById("messages");
const composerEl = document.getElementById("composer");
const inputEl = document.getElementById("message-input");
const resetBtn = document.getElementById("reset-btn");
const chips = document.querySelectorAll(".chip");

function scrollToBottom() {
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

function addMessage(text, role, meta) {
  const wrap = document.createElement("div");
  wrap.className = `msg ${role}` + (meta && meta.escalated ? " escalated" : "");

  const bubble = document.createElement("div");
  bubble.className = "msg-bubble";
  bubble.textContent = text;
  wrap.appendChild(bubble);

  if (meta && role === "bot") {
    const metaEl = document.createElement("div");
    metaEl.className = "msg-meta";
    metaEl.textContent = meta.escalated
      ? `↳ escalated to human · reason: ${meta.matched_intent ? meta.matched_intent : "n/a"}`
      : meta.matched_intent
        ? `↳ matched: ${meta.matched_intent} · confidence ${meta.confidence}`
        : "";
    if (metaEl.textContent) wrap.appendChild(metaEl);
  }

  messagesEl.appendChild(wrap);
  scrollToBottom();
}

function addTypingIndicator() {
  const wrap = document.createElement("div");
  wrap.className = "msg bot";
  wrap.id = "typing-indicator";
  wrap.innerHTML = `<div class="msg-bubble"><span class="typing"><span></span><span></span><span></span></span></div>`;
  messagesEl.appendChild(wrap);
  scrollToBottom();
}

function removeTypingIndicator() {
  const el = document.getElementById("typing-indicator");
  if (el) el.remove();
}

async function sendMessage(text) {
  addMessage(text, "user");
  addTypingIndicator();

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text }),
    });
    const data = await res.json();
    removeTypingIndicator();

    if (!res.ok) {
      addMessage("Something went wrong on my end — please try again.", "bot");
      return;
    }

    addMessage(data.reply, "bot", {
      escalated: data.escalated,
      matched_intent: data.matched_intent,
      confidence: data.confidence,
    });
  } catch (err) {
    removeTypingIndicator();
    addMessage("I couldn't reach the server. Is the Flask app still running?", "bot");
  }
}

composerEl.addEventListener("submit", (e) => {
  e.preventDefault();
  const text = inputEl.value.trim();
  if (!text) return;
  inputEl.value = "";
  sendMessage(text);
});

chips.forEach((chip) => {
  chip.addEventListener("click", () => {
    sendMessage(chip.dataset.q);
  });
});

resetBtn.addEventListener("click", async () => {
  await fetch("/api/reset", { method: "POST" });
  location.reload();
});
