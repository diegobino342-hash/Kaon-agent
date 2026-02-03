import threading
import asyncio
import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from engine import KaonEngine

# Configura a pasta frontend para servir os arquivos estáticos
app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

# Inicializa a entidade única do motor
engine = KaonEngine()

def run_engine_thread():
    """Inicia o loop assíncrono do motor em uma thread paralela"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(engine.scan_market())

# Dispara o motor neural 24/7
threading.Thread(target=run_engine_thread, daemon=True).start()

@app.route('/')
def serve_dashboard():
    """Entrega o Web App pronto ao acessar a URL"""
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/status')
def get_kaon_status():
    """Endpoint de telemetria para o celular"""
    return jsonify({
        "pair": engine.current_pair,
        "price": engine.last_price,
        "signal": engine.active_signal,
        "neural_memory": "active",
        "is_learning": True
    })

if __name__ == "__main__":
    # A Render exige o uso da porta definida pela variável de ambiente PORT
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
