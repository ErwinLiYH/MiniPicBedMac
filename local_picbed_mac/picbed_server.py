from flask import Flask, send_from_directory
from . import FILES_DIRECTORY


app = Flask(__name__)

@app.route(f'/<vault>/<filename>')
def serve_file(vault, filename):
    return send_from_directory(FILES_DIRECTORY[vault], filename)
