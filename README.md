# M416 — Offline AI Voice Assistant

M416 is a modular offline AI voice assistant built using Python, local LLMs, speech recognition, and persistent memory systems.

The assistant supports:
- wake-word activation,
- natural language understanding,
- local AI reasoning,
- conversational responses,
- application control,
- persistent memory storage,
- offline execution workflows.

The project is designed as a local-first AI agent architecture with modular orchestration, tool routing, and extensible command execution.

---

# Features

## Voice Interaction
- Wake-word activation ("M416")
- Speech-to-text command processing
- Offline text-to-speech responses

## AI Reasoning
- Local LLM-powered intent parsing
- Conversational response generation
- Structured tool routing pipeline

## Tool Execution
- Open desktop applications
- Google/web search fallback
- Time/date retrieval
- Remembering and Fetching where user items are placed

## Persistent Memory
- Store custom user memories
- Retrieve stored contextual information
- SQLite-backed memory system

## Assistant Architecture
- Modular orchestration pipeline
- Intent classification layer
- Tool abstraction system
- Conversational fallback handling

---

# Tech Stack

## Core
- Python

## AI / LLM
- Ollama
- Qwen2.5:3B

## Speech
- SpeechRecognition
- Windows SAPI (offline TTS)

## Database
- SQLite3

## Architecture
- Modular tool routing
- Local-first execution pipeline
- AI intent orchestration

---

# Project Structure

```text
M416/
│
├── main.py          # Main assistant orchestration loop
├── intent.py        # LLM-powered intent parser
├── chat.py          # Conversational response generation
├── tools.py         # System tools and automation
├── memo.py          # SQLite memory system
├── voice.py         # Offline text-to-speech layer
│
├── memory.db        # Persistent assistant memory
├── README.md
└── .gitignore
```

---

# Setup

## 1. Clone Repository

```bash
git clone <your_repo_link>
cd M416
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows
```bash
source venv/Scripts/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download:
https://ollama.com/

Install required model:

```bash
ollama run qwen2.5:3b
```

---

## 5. Run Assistant

```bash
python main.py
```

---

# Future Roadmap

- Multi-step task chaining
- Cloud-based LLM routing
- WhatsApp/message automation
- Browser automation
- Long-term memory system
- Context-aware conversations
- Smart authentication layer
- Hybrid online/offline architecture

---

# Disclaimer

This project is an experimental local AI assistant built for learning, automation, and AI-agent architecture exploration.