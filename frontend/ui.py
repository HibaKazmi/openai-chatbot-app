import gradio as gr
from services.chatbot import ask_llm

def gradio_chat(prompt):
    return ask_llm(prompt)

gui = gr.Interface(
    fn=gradio_chat,
    inputs=gr.Textbox(lines=2, placeholder="Ask me..."),
    outputs="text",
    title="GenAI Chat",
    description="Chatbot using OpenAI, FastAPI, Gradio, and SQLite",
    theme="default"
)