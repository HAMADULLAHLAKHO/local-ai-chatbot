# local-ai-chatbot
A conversational AI chatbot built with Python, Ollama, and Qwen 2.5.
# Local AI Chatbot Using Python and Ollama

A beginner-friendly conversational AI chatbot built with Python, Ollama, and the Qwen 2.5 language model. It runs locally on your computer without requiring a paid cloud AI API.

## Features

- Answers general questions using a local AI model.
- Supports continuous conversations in the terminal.
- Maintains conversation history during the current session.
- Includes basic connection error handling.
- Uses a local Ollama service instead of a paid AI API.

## Technologies Used

- Python
- Ollama
- Qwen 2.5 (0.5B)
- Requests library
- HTTP API communication

## Requirements

Before running the chatbot, install:

1. Python
2. Ollama for Windows: https://ollama.com/download/windows
3. The Qwen 2.5 (0.5B) model

## Installation and Setup

### 1. Download the project

Download or clone this repository to your computer.

### 2. Install the Python dependency

Open a terminal in the project folder and run:

```bash
python -m pip install requests
```

### 3. Download the AI model

Run:

```bash
ollama run qwen2.5:0.5b
```

Wait for the model to download. You can test it with a message, then type `/bye` to exit the model's chat.

### 4. Run the chatbot

Make sure Ollama is running, then execute:

```bash
python chatbot.py
```

### 5. Start chatting

Enter a message at the `You:` prompt. To end the session, type:

```text
exit
```

## How It Works

The Python program sends user messages to Ollama's local HTTP API. Ollama processes the messages using the selected Qwen model and returns a response, which the program displays in the terminal.

## Limitations

- Response quality depends on the model and the computer's available resources.
- The model must be downloaded before it can be used offline.
- The chatbot currently uses a terminal-based interface.
- Conversation history is maintained only during the current session.

## Future Improvements

- Add a graphical user interface.
- Improve conversation history management.
- Add configurable model selection.
- Improve error handling and user experience.

## Author

Developed as a learning project to explore Python programming and local AI application development.
