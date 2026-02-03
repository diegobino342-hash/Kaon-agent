from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import agent

app = Flask(__name__, static_folder="../frontend")
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
    return send_from_directory("../frontend", "index.html")

@app.route("/app/<path:path>")
def static_files(path):
    return send_from_directory("../frontend", path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
