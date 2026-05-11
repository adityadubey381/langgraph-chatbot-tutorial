````markdown
# LangGraph Chatbot Tutorial

A practical repository for learning how to build AI chatbots using LangGraph, LangChain, Streamlit, MCP, tools, memory, databases, and RAG pipelines.

This project focuses on understanding modern AI orchestration, graph-based workflows, conversational memory, streaming responses, tool calling, and retrieval-augmented generation (RAG) using real implementations instead of only theory.

---

# Repository Link

https://github.com/adityadubey381/langgraph-chatbot-tutorial

---

# Features

- LangGraph chatbot workflows
- Stateful conversation handling
- Streamlit frontend integration
- MCP integration
- Tool calling support
- Database-backed memory
- Async chatbot architecture
- Streaming responses
- RAG implementation
- Modular backend structure

---

# Tech Stack

- Python
- LangChain
- LangGraph
- Streamlit
- SQLite
- OpenAI API
- dotenv

---

# Project Structure

```text
langgraph-chatbot-tutorial/
│
├── chatbot_async.py
├── chatbot_mcp.py
├── langgraph_backend.py
├── langgraph_database_backend.py
├── langgraph_mcp_backend.py
├── langgraph_tool_backend.py
├── langgraph_rag_backend.py
│
├── streamlit_frontend.py
├── streamlit_frontend_database.py
├── streamlit_frontend_mcp.py
├── streamlit_frontend_streaming.py
├── streamlit_frontend_threading.py
├── streamlit_frontend_tool.py
├── streamlit_rag_frontend.py
│
├── requirements.txt
├── .gitignore
└── README.md
````

---

# Topics Covered

## 1. LangGraph Basics

* StateGraph
* Nodes and edges
* Workflow execution
* State management

## 2. Chatbot Development

* Conversational AI
* Chat history
* Context handling
* Response generation

## 3. Streamlit Frontend

* Interactive chatbot UI
* Streaming responses
* Frontend-backend communication

## 4. Database Integration

* SQLite storage
* Persistent memory
* Chat history management

## 5. MCP Integration

* MCP architecture
* Model Context Protocol workflows

## 6. Tool Calling

* External tools
* AI tool execution
* Function calling workflows

## 7. RAG (Retrieval-Augmented Generation)

* Document retrieval
* Context injection
* Knowledge-enhanced chatbot systems

---

# Installation

## Clone Repository

```bash
git clone https://github.com/adityadubey381/langgraph-chatbot-tutorial.git

cd langgraph-chatbot-tutorial
```

---

# Create Virtual Environment

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

# Run the Application

## Streamlit Frontend

```bash
streamlit run streamlit_frontend.py
```

## Database Version

```bash
streamlit run streamlit_frontend_database.py
```

## MCP Version

```bash
streamlit run streamlit_frontend_mcp.py
```

## RAG Version

```bash
streamlit run streamlit_rag_frontend.py
```

---

# Learning Objectives

This repository helps in learning:

* Modern AI chatbot architecture
* LangGraph workflows
* AI orchestration
* Stateful AI systems
* Tool-augmented LLMs
* Streaming AI applications
* Retrieval pipelines
* Production-oriented GenAI systems

---

# Future Improvements

* Multi-agent systems
* Vector database integration
* Voice chatbot support
* Authentication system
* Docker deployment
* Cloud deployment
* LangSmith observability
* Advanced memory systems

---

# Author

## Aditya Kumar Dubey

* GitHub: [https://github.com/adityadubey381](https://github.com/adityadubey381)
* LinkedIn: [https://www.linkedin.com/in/aditya-kumar-dubey-9833b4278/](https://www.linkedin.com/in/aditya-kumar-dubey-9833b4278/)

---

# License

This project is created for educational and learning purposes.

```
```
