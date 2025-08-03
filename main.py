from api.routes import app
from frontend.ui import gui
from db.database import init_db
import threading
import uvicorn

if __name__ == "__main__":
    init_db()
    def run_api():
        uvicorn.run(app, host="0.0.0.0", port=8000)

    def run_ui():
        gui.launch(server_name="localhost", server_port=7860)

    threading.Thread(target=run_api).start()
    run_ui()