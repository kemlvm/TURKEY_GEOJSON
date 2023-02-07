from subprocess import Popen


def load_jupyter_server_extension(nbapp):
    Popen(
        [
            "streamlit",
            "run",
            "streamlit_app.py",
            "--browser.serverAddress=0.0.0.0",
            "--server.enableCORS=False",
        ]
    )
