from .picbed_server import app
from .picbed_GUI import ClipboardImageSaverApp
from . import PORT

from threading import Thread


# start the server in a separate thread
def run_server():
    app.run(port=PORT)

server_thread = Thread(target=run_server, daemon=True)
server_thread.start()

# start the GUI app
GUI_app = ClipboardImageSaverApp()
GUI_app.run()