from openai import AsyncOpenAI
from context import TWIN_SYSTEM_PROMPT
from tools import tools
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, SQLiteSession
from styles import CSS, JS, EXAMPLES
from dotenv import load_dotenv
import gradio as gr
import logging
import os

load_dotenv(override=True)
set_tracing_disabled(True)

logger = logging.getLogger("digital_twin")
logging.basicConfig(level=logging.INFO)

FALLBACK_MESSAGE = (
    "Sorry, I'm having trouble responding right now. Please try again in a moment."
)

MODEL_NAME = "openai/gpt-oss-120b" #"llama-3.3-70b-versatile" #
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
groq_client = AsyncOpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url=GROQ_BASE_URL,
)
groq_model = OpenAIChatCompletionsModel(
    model=MODEL_NAME,  # or any Groq-hosted model
    openai_client=groq_client,
)
session = SQLiteSession("12346")

twin_agent = Agent(
    name="Digital Twin",
    instructions=TWIN_SYSTEM_PROMPT,
    model=groq_model,
    tools=tools,
)

async def chat(message, _history):
    # conversation history is persisted via SQLiteSession, not gradio's history param
    try:
        result = await Runner.run(twin_agent, message, session=session)
        return result.final_output
    except Exception:
        logger.exception("Chat request failed")
        return FALLBACK_MESSAGE


if __name__ == "__main__":
    gr.ChatInterface(
        chat,
        examples=EXAMPLES,
        title="Digital Twin",
        description="Talk to my AI twin about my career",
        chatbot=gr.Chatbot(show_label=False),
    ).launch(
        css=CSS,
        js=JS,
        theme=gr.themes.Base(),
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860)),
    )
