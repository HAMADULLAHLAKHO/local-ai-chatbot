
import requests

print("AI Chatbot Started!")
print("Type 'exit' to stop the chatbot.\n")

while True:
    user_message = input("You: ")

    if user_message.lower().strip() == "exit":
        print("Bot: Goodbye!")
        break

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "qwen2.5:0.5b",
            "messages": [
                {"role": "user", "content": user_message}
            ],
            "stream": False
        }
    )

    if response.ok:
        answer = response.json()["message"]["content"]
        print("Bot:", answer)
    else:
        print("Error:", response.text)
