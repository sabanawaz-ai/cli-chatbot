# CLI Chatbot

A command-line chatbot built in Python using Groq's LLM API. This repo 
contains two versions, built while learning how LLM APIs, conversation 
memory, and Python fundamentals work together.

## Files

- **`chatbasic.py`** — A minimal chatbot with no memory. Each message is 
  sent independently, with no awareness of previous messages in the 
  conversation.
- **`chatwithmemory.py`** — A more complete version that maintains full 
  conversation history in memory during a session, and persists that 
  history to a local `history.json` file — so conversations survive 
  even after restarting the program.

## Tech used

- Python 3
- [Groq API](https://groq.com) (`openai/gpt-oss-20b` model)
- Python's built-in `json` module for saving conversation history

## How it works

Both scripts follow a REPL (Read-Evaluate-Print-Loop) pattern:
1. Read the user's input from the terminal
2. Send it (plus prior conversation history, in the memory version) to 
   the Groq API
3. Print the model's reply
4. Loop back and repeat until the user types `quit`

The key difference is that `chatwithmemory.py` keeps a growing list of 
every message exchanged and resends the entire conversation on each 
turn — since the API itself is stateless and has no memory between 
calls. It also saves that list to a JSON file after every exchange, so 
the conversation can be reloaded on the next run.

## Setup

1. Clone this repo:
```bash
   git clone https://github.com/iamsabanawaz/cli-chatbot.git
   cd cli-chatbot
```

2. Create and activate a virtual environment:
```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
   pip install groq
```

4. Set your Groq API key:
```bash
   export GROQ_API_KEY="your-key-here"
```
   Get a free key at [console.groq.com/keys](https://console.groq.com/keys).

## Usage

Run the basic version (no memory):
```bash
python chatbasic.py
```

Run the version with persistent memory:
```bash
python chatwithmemory.py
```

Type `quit` at any time to exit.

## What I learned

- How LLM APIs actually work: requests, JSON payloads, tokens, and 
  responses
- Why LLM APIs are stateless, and how to implement conversation memory 
  by resending full message history on each turn
- Persisting application state to disk using Python's `json` module
- Setting up and managing a Python virtual environment
- Debugging real API issues: authentication errors, invalid model 
  names, rate limits (429), and payload size limits (413)
- Version control basics with git and GitHub, including resolving 
  merge conflicts between local and remote history

## Possible next steps

- Add a system prompt to give the bot a defined personality/role
- Add error handling (`try`/`except`) around API calls
- Support switching models via a command-line flag