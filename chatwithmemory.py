import json
import os
from groq import Groq

client = Groq()

HISTORY_FILE = "history.json"

# Load previous conversation if it exists, otherwise start fresh
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r") as f:
        messages = json.load(f)
    print("Loaded previous conversation.\n")
else:
    messages = []

print("Chat with Groq! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        max_tokens=500
    )

    reply = response.choices[0].message.content

    messages.append({"role": "assistant", "content": reply})

    print(f"Groq: {reply}\n")

    # Save after every exchange, so nothing is lost even if the program crashes
    with open(HISTORY_FILE, "w") as f:
        json.dump(messages, f, indent=2)