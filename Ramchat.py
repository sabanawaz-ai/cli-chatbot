
from groq import Groq

client = Groq()  # reads GROQ_API_KEY from environment automatically

messages = []  # this list holds the whole conversation — our "memory"

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