# 🤖 AI Agents & LLM Learning Journey

Welcome to my learning repository where I explore AI Agents and modern LLM frameworks. This project documents my hands-on practice with building intelligent agents, workflows, and tool integrations.

## 📚 Topics Covered

- **LangChain:** Multi-model integration (Google Gemini, OpenAI, Groq), tool calling, structured outputs, streaming, and middleware.
- **LangGraph:** Stateful chatbots, cyclical agent graphs, memory persistence, and Human-in-the-Loop workflows.
- **Model Context Protocol (MCP):** Creating FastMCP tool servers and connecting multi-server clients to agents.

## 📁 Folder Structure

- `langchain/` – Notebooks on LangChain fundamentals, prompts, structured output, and middleware.
- `langgraph/` – StateGraph workflows, chatbot examples, and human feedback loops.
- `MCP/` – FastMCP weather server and multi-server MCP client scripts.
- `main.py` – Helper script to verify configured API keys and test model connectivity.

## 🛠️ Technologies Used

- **Language & Frameworks:** Python, LangChain, LangGraph
- **Protocols & Tools:** Model Context Protocol (MCP), Tavily Search
- **LLM Providers:** Google Gemini, OpenAI, Groq (Llama & Qwen)
- **Utilities:** Pydantic, python-dotenv, uv

## ⚙️ Getting Started

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Setup environment variables:** Create a `.env` file in the root folder with placeholder keys:
   ```env
   GOOGLE_API_KEY="your-google-api-key"
   OPENAI_API_KEY="your-openai-api-key"
   GROQ_API_KEY="your-groq-api-key"
   TAVILY_API_KEY="your-tavily-api-key"
   ```
3. **Verify setup:**
   ```bash
   python main.py
   ```

## 🎯 Next Learning Goals

- [ ] Retrieval-Augmented Generation (RAG)
- [ ] Multi-agent collaboration systems
- [ ] Agent evaluation with LangSmith

## 👤 Author

**Divya Bisht** — Passionate about Generative AI, Agentic workflows, and LLM development.
