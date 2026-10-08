# Gemini Streaming Chatbot ⚡

A terminal chatbot powered by Google Gemini that streams responses live, word by word, and remembers the conversation.



## Features
- **Live streaming:** responses appear as they're generated, instead of after a long wait
- **Conversation memory:** remembers the last 20 messages, so you can ask follow-up questions
- **Custom system prompt:** controls the assistant's tone and behavior
- **Error handling:** if a request fails, the chatbot keeps running instead of crashing

## What I learned
- How to call an LLM API from Python
- How streaming works: the model sends small chunks as it generates them
- LLMs have no memory by themselves. The "memory" is just past messages sent again with every request
- Why history needs a limit (more history = more tokens = slower and costlier)
- Keeping API keys safe with `.env` files

## Tech stack
Python · Google Gemini API (`google-genai`) · python-dotenv

## Run it yourself
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file and add: `GEMINI_API_KEY=your_key_here`
4. Run: `python main.py`
5. Type `bye`, `exit` or `stop` to quit
