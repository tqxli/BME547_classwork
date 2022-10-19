# server.py
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def server_status():
    return "Server is on."