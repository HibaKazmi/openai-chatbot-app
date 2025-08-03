GenAI Chatbot Project
A simple AI-powered chatbot using OpenAI, FastAPI, Gradio, and SQLite.
This project showcases how to build a full-stack conversational chatbot with a modern frontend and backend.
Features
- Chatbot interface built with Gradio
- Backend API built with FastAPI
- AI responses powered by OpenAI GPT-3.5 Turbo
- Stores chat history locally in SQLite
- Reads the API key securely from a `.env` file
Setup Instructions
1. Clone the Repository

```bash
git clone <your-repo-url>
cd gen_ai_proj1
```

2. Create and Activate a Virtual Environment (Recommended)

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install Project Dependencies

Option 1: From `requirements.txt` (if available)

```bash
pip install -r requirements.txt
```

Option 2: Install Manually

```bash
pip install fastapi uvicorn gradio openai python-dotenv
```

4. Add Your OpenAI API Key

Create a `.env` file in the root of your project and add this line:

```
OPENAI_API_KEY=your-openai-api-key-here
```

Important:

You must have an active OpenAI billing setup to use the API. Your account must have either:
- A valid payment method attached OR
- At least $5 in free credit

Without this, API requests will fail with:
openai.RateLimitError: code: 'insufficient_quota'

You can manage billing and usage here:
https://platform.openai.com/account/usage

5. Run the Project

```bash
python main.py
```

- FastAPI server: http://localhost:8000
- Gradio UI: http://localhost:7860
Troubleshooting
- Ensure all subfolders (e.g. `api/`, `db/`, `services/`) contain an `__init__.py` file.
- Always run the project from the root folder.
- If the Gradio UI shows "Error", check your terminal for the traceback.
- Confirm your `.env` file is in the root directory and properly formatted.
- Make sure your OpenAI key is valid and has billing access.
Project Structure
gen_ai_proj1/
├── api/           # FastAPI routes
├── db/            # SQLite DB utilities
├── frontend/      # Gradio UI components
├── models/        # Pydantic models
├── services/      # OpenAI service and business logic
├── main.py        # Project entry point
├── .env           # API key config
├── README.md      # You're reading it!
Tech Stack
- OpenAI GPT-3.5
- FastAPI
- Gradio
- SQLite
- Python Dotenv
Notes
- This chatbot is built for local testing and prototyping.
- You can extend it with authentication, advanced memory, or larger DB.
- Never commit your `.env` or API key to GitHub.
Questions?
Feel free to open an issue or reach out.
