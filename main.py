# ============================================================
#  DecodeLabs | Industrial Training Kit — Batch 2026
#  Project 1 : Rule-Based AI Chatbot
#  Architecture: IPO Model  →  Input → Process → Output
#  Pattern    : Dictionary / Hash-Map  O(1)  (NOT if-elif ladder)
# ============================================================

# ── KNOWLEDGE BASE (Hash Map — O(1) lookup) ──────────────────
RESPONSES = {
    # Greetings
    "hello"        : "Hey there! 👋 I'm DecoBot. How can I assist you today?",
    "hi"           : "Hi! Welcome to DecodeLabs. What can I do for you?",
    "hey"          : "Hey! Great to see you. Ask me anything!",
    "good morning" : "Good morning! ☀️ Ready to build something amazing today?",
    "good evening" : "Good evening! 🌙 Hope your day went well. How can I help?",

    # Identity / About
    "who are you"  : "I'm DecoBot 🤖 — a rule-based AI chatbot built at DecodeLabs as Project 1.",
    "what are you" : "I'm a deterministic chatbot. My responses are 100% hard-coded — zero hallucination risk!",
    "your name"    : "My name is DecoBot. Built with pure Python logic by a DecodeLabs intern!",

    # DecodeLabs Info
    "what is decodelabs" : "DecodeLabs is a tech training organisation based in Greater Lucknow, India. 🇮🇳",
    "decodelabs"         : "DecodeLabs powers hands-on AI/ML industrial training for the next generation of engineers.",
    "contact"            : "📞 +91 89330 06408 | ✉ decodelabs.tech@gmail.com | 🌎 www.decodelabs.tech",

    # AI / Project concepts
    "what is ai"          : "AI is the simulation of human intelligence by machines using logic, data, and algorithms.",
    "what is a chatbot"   : "A chatbot is a program that simulates conversation. I'm a rule-based one — I use a dictionary, not a neural network!",
    "what is rule based"  : "Rule-based AI uses explicit if-else / dictionary logic. Every output is traceable — that's the 'white box' advantage.",
    "what is machine learning" : "ML lets machines learn patterns from data without being explicitly programmed. That's Project 2 territory! 😄",
    "what is ipo model"   : "IPO = Input → Process → Output. It's the foundational blueprint for transparent AI systems.",
    "difference between ai and ml" : "AI is the broad concept of machines mimicking intelligence. ML is a *subset* of AI where the machine learns from data.",

    # Small talk / Emotions
    "how are you"   : "I'm running at 100% efficiency! No bugs detected. 🟢 How about you?",
    "i am fine"     : "Great to hear! Let's keep building! 💪",
    "thank you"     : "You're welcome! Keep coding and keep learning. 🚀",
    "thanks"        : "Anytime! That's what I'm here for. 😊",
    "help"          : "Sure! You can ask me about AI, DecodeLabs, this project, or just chat. Type 'exit' to quit.",
    "what can you do" : "I can answer questions about AI, ML, this project, and DecodeLabs. I run on pure logic — no LLM needed!",

    # Fun
    "tell me a joke" : "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂",
    "motivate me"    : "Every expert was once a beginner. Your first rule-based bot is the skeleton of your future AI empire. BUILD IT. 🔥",
}

# ── DEFAULT FALLBACK ─────────────────────────────────────────
FALLBACK = "🤔 I don't understand that yet. Try asking about AI, DecodeLabs, or type 'help'."

# ── EXIT KEYWORDS (Kill Command) ─────────────────────────────
EXIT_COMMANDS = {"exit", "quit", "bye", "goodbye", "stop"}


# ════════════════════════════════════════════════════════════
#  PHASE 1 — INPUT & SANITIZATION
# ════════════════════════════════════════════════════════════
def sanitize(raw: str) -> str:
    """Normalize input: lowercase + strip whitespace."""
    return raw.lower().strip()


# ════════════════════════════════════════════════════════════
#  PHASE 2 — PROCESS  (Intent Matching — O(1) Dictionary)
# ════════════════════════════════════════════════════════════
def get_response(clean_input: str) -> str:
    """
    Look up the cleaned input in the knowledge base.
    Falls back to FALLBACK if intent is unknown.
    Uses .get() — atomic lookup + fallback in one operation.
    """
    return RESPONSES.get(clean_input, FALLBACK)


# ════════════════════════════════════════════════════════════
#  PHASE 3 — OUTPUT + FEEDBACK LOOP  (Infinite While Loop)
# ════════════════════════════════════════════════════════════
def run_chatbot():
    print("=" * 55)
    print("  🤖  DecoBot — Rule-Based AI Chatbot")
    print("  DecodeLabs Industrial Training Kit | Batch 2026")
    print("  Type 'help' for options. Type 'exit' to quit.")
    print("=" * 55)

    # ── THE HEARTBEAT: INFINITE LOOP ─────────────────────────
    while True:
        # Phase 1 — Input
        raw_input = input("\nYou: ")
        clean_input = sanitize(raw_input)          # sanitize

        # Exit Strategy — Kill Command
        if clean_input in EXIT_COMMANDS:
            print("DecoBot: Goodbye! Keep building, keep learning. 👋🚀")
            break

        # Phase 2 — Process  (O(1) dictionary lookup)
        reply = get_response(clean_input)

        # Phase 3 — Output
        print(f"DecoBot: {reply}")


# ── ENTRY POINT ──────────────────────────────────────────────
if __name__ == "__main__":
    run_chatbot()
