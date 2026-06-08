# Project 1: Rule-Based AI Chatbot (DecoBot)

Welcome to the repository for **Project 1: DecoBot**, completed during my **Artificial Intelligence Engineering Internship** at **DecodeLabs** (Batch 2026). 

This project serves as the vital foundational phase of my industrial training, focusing on constructing deterministic **Control Flow and Logic** systems.

---

## 🚀 Project Goal & Features

The objective of this milestone is to construct a continuous digital loop that successfully simulates human conversation through rule-based decision-making. 

### Key Technical Achievements in My Code:
* **The Heartbeat Loop:** Runs seamlessly inside an infinite `while True` loop until a kill instruction is triggered.
* **Input Sanitization & Normalization Pipeline:** Processes raw user queries by lowercasing and stripping padding whitespaces to achieve deterministic logic matching.
* **$O(1)$ Complexity Engine:** Replaced the inefficient, traditional `if-elif-else` conditional ladder with an optimized **Dictionary / Hash-Map** lookup architecture for near-instantaneous response generation.

---

## 🧠 Architectural Framework: The IPO Model

The application strictly obeys the classic **Input-Process-Output (IPO)** engineering blueprint:### Phase 1: Input & Sanitization
To guarantee logic durability and protect against accidental spacing or casing variations, the text transformation pipeline uses:
* `.lower()` for casing normalization.
* `.strip()` for leading and trailing whitespace trimming.

$$\text{"  HeLLo "} \xrightarrow{\text{.lower().strip()}} \text{"hello"}$$

### Phase 2: Processing via Optimized Hash-Mapping
Instead of evaluating conditions line-by-line, the application stores its pre-defined knowledge base inside a key-value data structure (`RESPONSES`).
* **Atomic Lookups:** Utilizes the Python `.get()` method to check intents in constant $O(1)$ time complexity.
* **Fallback Strategy:** If an intent is unrecognized, the engine avoids compilation failures by defaulting gracefully to a hard-coded error handling block (`FALLBACK`).

### Phase 3: Output & Exit Strategy
* **Kill Commands:** The engine continuously listens for exit parameters (`exit`, `quit`, `bye`, `close`) to terminate the session loop safely.
* **System Help Desk:** Intercepts the `help` keyword to dynamically print available operational directories to the user interface.

---

## 🛠️ Key Skills Demonstrated
* **Advanced Data Structuring:** Implementing optimized dictionary lookups in place of deep conditional nesting.
* **Deterministic Engine Configuration:** Constructing structured "white-box" flows with a 0% hallucination rate.
* **Text Preprocessing Pipelines:** Building fault-tolerant data sanitation workflows in Python.

---

## ⚙️ Supported Mapped Intests Include:
* **Greetings:** `hello`, `hi`, `hey`, `good morning`, `good evening`
* **Identity Profiles:** `who are you`, `what are you`, `your name`
* **Corporate Profile:** `what is decodelabs`, `decodelabs`
* **Utility Triggers:** `help`, `features`, `clear`

---
*Developed as part of the Industrial Training Kit under DecodeLabs (Batch 2026).*
