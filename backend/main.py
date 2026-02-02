import json
from backend.ws.pusher_client import PusherClient
from backend.ws.channel_manager import ChannelManager
from backend.core.kaon_engine import KaonEngine

engine = KaonEngine()

def on_message(ws, message):
    data = json.loads(message)
    if "data" in data and "price" in data["data"]:
        payload = json.loads(data["data"])
        engine.process_tick(payload["timestamp"], payload["price"])

client = PusherClient(on_message)
client.connect()
