# LangGraph-Conversational-ChatBot

A conversational AI chatbot built using **LangGraph**, **Hugging Face Qwen 2.5**, and **Streamlit**. The application supports multi-turn conversations with persistent memory using LangGraph's checkpointer mechanism.

---

## Features

* Built with LangGraph workflow orchestration
* Uses Qwen/Qwen2.5-7B-Instruct from Hugging Face
* Persistent conversation memory with InMemorySaver
* Interactive Streamlit chat interface
* Thread-based conversation management
* Easy to extend with additional tools and agents

---

## Project Structure

```text
.
├── chatbot.py
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

## Tech Stack

* Python
* LangGraph
* LangChain
* Hugging Face Inference API
* Qwen 2.5 7B Instruct
* Streamlit

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/LangGraph-Conversational-ChatBot.git

cd LangGraph-Conversational-ChatBot
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / Mac

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key
```

Get your API key from:

https://huggingface.co/settings/tokens

---

## Run the Application

```bash
streamlit run app.py
```

---

## How It Works

1. User enters a message in the Streamlit UI.
2. Message is passed to LangGraph.
3. LangGraph executes the ChatNode.
4. Qwen 2.5 model generates a response.
5. Conversation history is stored using InMemorySaver.
6. Response is streamed back to the user.

---

## LangGraph Workflow

```text
START
  │
  ▼
ChatNode
  │
  ▼
 END
```

---

## Future Improvements

* Add Google Gemini support
* Add OpenAI models
* Add tool calling
* Add RAG (Document Q&A)
* Add database memory
* Add multi-agent workflows

---

## Requirements

```text
langgraph
langchain
langchain-core
langchain-huggingface
huggingface-hub
streamlit
python-dotenv
typing-extensions
```

---

## License

MIT License

---

### Author

**Harsh Saini**

Aspiring AI/ML & Generative AI Engineer passionate about building intelligent applications using LangChain, LangGraph, LLMs, and modern AI technologies.
