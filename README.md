# Agentic Chatbot with LangGraph, LangChain, and Python

This project demonstrates how to build an **agentic chatbot** using [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://github.com/langchain-ai/langchain), and Python. The chatbot leverages agentic workflows to handle complex, multi-step conversations with users.

## Features

- **Agentic Reasoning:** The chatbot can plan, reason, and execute tasks using agent-based logic.
- **Modular Design:** Built with LangGraph for flexible conversational flows.
- **Extensible:** Easily add new tools, memory, or integrations.
- **Supports OpenAI and Groq Models:** Works with both OpenAI and Groq LLMs via API keys.

## Requirements

- Python 3.8+
- `langchain`
- `langgraph`
- `streamlit`
- (Optional) OpenAI API key or Groq API key

## Usage

1. **Clone the repository:**
    ```bash
    git clone https://github.com/abhinavranjan-ai/chatbot-agenticai.git
    cd chatbot-agenticai

## Installation

```bash
pip install -r requirements.txt
```


2. **Configure your environment:**
    - Launch the app and enter your OpenAI or Groq API key in the Streamlit UI when prompted.

3. **Run the chatbot app:**
    ```bash
    streamlit run app.py
    ```

## How It Works

- **LangChain** provides the language model interface and agent tools.
- **LangGraph** manages the conversational flow as a graph, enabling complex agentic behaviors.
- **Streamlit** powers the user interface, allowing users to input their API keys and interact with the chatbot.
- The chatbot receives user input, reasons about the task, and responds or takes actions accordingly.

## Example

```
User: What's the weather in Paris and set a reminder for tomorrow.
Bot: The weather in Paris is sunny. Reminder set for tomorrow.
```

## Customization

- Add new tools or memory modules in `chatbot.py`.
- Modify the agent's reasoning logic using LangChain's agent framework.


> **Note:** If you find this project helpful, feel free to [follow me on LinkedIn](https://www.linkedin.com/in/abhinav-ranjan-ai/)!
