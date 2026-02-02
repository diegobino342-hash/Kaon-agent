from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

last_signal = None

@app.route("/signal")
def signal():
    return jsonify(last_signal or {})

@app.route("/")
def health():
    return {"status": "KAON ONLINE"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
