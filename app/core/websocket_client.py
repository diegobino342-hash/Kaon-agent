import websocket
import json
from logger import log
from collections import defaultdict
from core.candle_builder import CandleBuilder
from config import WS_HOST, WS_PARAMS

class WebSocketClient:
    def __init__(self):
        self.ws = None
        self.candles = defaultdict(CandleBuilder)

    def connect(self):
        self.ws = websocket.create_connection(WS_HOST + WS_PARAMS)
        log("WebSocket conectado")

    def subscribe(self, symbol):
        self.ws.send(json.dumps({
            "event": "pusher:subscribe",
            "data": {"auth": "", "channel": symbol}
        }))

    def unsubscribe(self, symbol):
        self.ws.send(json.dumps({
            "event": "pusher:unsubscribe",
            "data": {"channel": symbol}
        }))

    def get_candles(self, symbol):
        return self.candles[symbol].get()
