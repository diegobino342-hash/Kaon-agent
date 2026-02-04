from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import agent
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="/")
CORS(app)

# inicia o agente automaticamente
agent.start()

@app.route("/")
def health():
    return {"status": "KAON ONLINE"}

@app.route("/signal")
def signal():
    return jsonify(agent.get_signal())

@app.route("/candles")
def candles():
    return jsonify(agent.get_candles())

@app.route("/app")
def frontend():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(FRONTEND_DIR, path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
