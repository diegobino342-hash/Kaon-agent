import websocket
import json
from config import WS_HOST, ORIGIN

class QuotexSocket:
    def __init__(self, on_tick):
        self.on_tick = on_tick

    def on_message(self, ws, message):
        data = json.loads(message)
        if "event" in data and "-OTC" in data["event"]:
            payload = json.loads(data["data"])
            self.on_tick(payload)

    def connect(self, symbol):
        self.ws = websocket.WebSocketApp(
            WS_HOST,
            header={"Origin": ORIGIN},
            on_message=self.on_message
        )
        self.ws.on_open = lambda ws: ws.send(json.dumps({
            "event": "pusher:subscribe",
            "data": {"auth": "", "channel": symbol}
        }))
        self.ws.run_forever()
