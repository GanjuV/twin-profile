---
title: twin
app_file: app.py
sdk: gradio
sdk_version: 6.14.0
---

# Digital Twin

An AI chatbot that acts as a digital twin, answering questions about a person's
career, background, skills, and experience. Built with [Gradio](https://www.gradio.app/)
for the chat UI and [Groq](https://groq.com/) (via the OpenAI-compatible API) for inference.

The twin's knowledge comes from a LinkedIn profile export (`linkedin.pdf`) and a
free-form summary (`summary.txt`), which are combined into a system prompt
(`context.py`). If a visitor asks something not covered by that context, the
twin records the question instead of guessing, and if a visitor wants to get
in touch, the twin records their email — both via push notifications ([ntfy.sh](https://ntfy.sh/)).

## Project structure

- `app.py` — Gradio chat interface and the main conversation loop with the LLM
- `context.py` — builds the system prompt from `linkedin.pdf` and `summary.txt`
- `tools.py` — tool definitions/handlers for recording user details and unknown questions
- `styles.py` — CSS/JS and UI constants for the Gradio interface
- `linkedin.pdf` — exported LinkedIn profile used as context
- `summary.txt` — freeform summary used as context

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

Create a `.env` file in the project root with your Groq API key:

```
GROQ_API_KEY=your-key-here
```

## Running

```bash
uv run app.py
```

This starts the Gradio app locally (see the terminal output for the URL).
