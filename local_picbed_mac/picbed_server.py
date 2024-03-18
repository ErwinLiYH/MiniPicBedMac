from flask import Flask, send_from_directory
from . import FILES_DIRECTORY


app = Flask(__name__)

@app.route('/files/<filename>')
def serve_file(filename):
    return send_from_directory(FILES_DIRECTORY, filename)
