# 🚀 Founder Knowledge Assistant

The **Founder Knowledge Assistant** is an AI-powered tool designed to assist users in retrieving and summarizing information about company founders and entrepreneurs. It leverages a specialized database of founder-related articles combined with web search capabilities to deliver accurate, concise, and up-to-date insights.

---

## ✨ Features

- **Founder Articles Search**: Quickly retrieve insights from an exclusive database focused on founders.
- **Web Search Integration**: Real-time information via the Tavily API.
- **Context Persistence**: Seamless, conversational interactions by remembering previous queries.
- **Lifecycle Logging**: Monitor agent performance and debug effortlessly.
- **Interactive Agent Loop**: Engage interactively to ask questions and obtain precise answers.

---

## 📂 Project Structure

```
.
├── agent_context.py              # Manages conversational context
├── agent_logger.py               # Lifecycle and event logging
├── basic_agent.py                # Basic agent example
├── more_realistic_agent.py       # Advanced agent implementation
├── models.py                     # Document and retrieval response models
├── prompts.py                    # Agent prompts and instructions
├── tools/
│   ├── retrieve_founder_articles.py   # Specialized database retrieval
│   ├── tavily_search.py               # Web search using Tavily API
├── utils.py                      # Logging and API utilities
├── openai-agents/                # Virtual environment
├── .gitignore                    # Git ignore rules
```

---

## 🛠️ Setup Instructions

### 📌 Prerequisites

- Python 3.12 or higher
- [Tavily API](https://tavily.com) account and API key
- OpenAI API key

### ⚙️ Installation

1. **Clone the Repository:**

```sh
git clone https://github.com/your-username/founder-knowledge-assistant.git
cd founder-knowledge-assistant
```

2. **Set Up Virtual Environment:**

```sh
python3 -m venv openai-agents
source openai-agents/bin/activate  # Windows: openai-agents\Scripts\activate
```

3. **Install Dependencies:**

```sh
pip install -r requirements.txt
```

4. **Configure Environment Variables:**

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
VECTORIZE_ENDPOINT=your_vectorize_endpoint
VECTORIZE_TOKEN=your_vectorize_token
```

---

## 🚦 Usage

### ▶️ Running the Agent

Start the interactive assistant with:

```sh
python more_realistic_agent.py
```

You'll be prompted about enabling verbose logging. You can then ask questions about founders and receive instant responses.

### 💬 Example Interaction

```
=== Founder Knowledge Assistant ===
Ask questions about founders. Type 'exit', 'quit', or 'q' to end.

Your question: Who founded Tesla?
[Source: Retrieved from web search]
Elon Musk, JB Straubel, Ian Wright, Martin Eberhard, and Marc Tarpenning co-founded Tesla.
```

---

## 📊 Logging

The project supports configurable logging for better debugging and monitoring:

- **AgentLogger**: Logs detailed messages (INFO, DEBUG, WARNING, ERROR).
- **AgentLifecycleLogger**: Tracks agent lifecycle events.

Enable verbose logging by setting `verbose_logging=True` when running the agent.

---

## 🔍 Tools

### 📖 Founder Articles Search

- Retrieve insights from the dedicated founder articles database.
- Requires `VECTORIZE_ENDPOINT` and `VECTORIZE_TOKEN`.

### 🌐 Tavily Web Search

- Real-time search capability via Tavily API.
- Requires `TAVILY_API_KEY`.

---

## 🧑‍💻 Development

### ➕ Adding New Tools

1. Define your tool function in the `tools` directory.
2. Decorate it with `@function_tool`.
3. Register the tool in the `tools` list inside `more_realistic_agent.py`.

### ✅ Testing

Run individual scripts or create unit tests for isolated components.

---

## 📜 License

Licensed under the MIT License. See the `LICENSE` file for details.

---

## 🤝 Contributing

Your contributions are warmly welcomed! Please open an issue or submit a pull request to suggest improvements or fixes.

---
