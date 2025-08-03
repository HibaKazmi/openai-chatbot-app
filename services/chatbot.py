from openai import OpenAI
from services.memory import store_interaction
from services.logger import logger
import os
from dotenv import load_dotenv
load_dotenv()

Client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(prompt: str) -> str:
    logger.info(f"Prompt: {prompt}")

    full_prompt = f"You are a helpful assistant. {prompt}"

    response = Client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": full_prompt}]
    )

    reply = response.choices[0].message.content
    store_interaction(prompt, reply)
    return reply