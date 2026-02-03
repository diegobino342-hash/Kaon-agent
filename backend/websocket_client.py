import websocket, json

class MarketSocket:
    def __init__(self, on_tick):
        self.on_tick = on_tick

    def on_message(self, ws, msg):
        data = json.loads(msg)
        if "event" in data and "-OTC" in data["event"]:
            tick = json.loads(data["data"])
            self.on_tick(tick)

    def connect(self, symbol):
        self.ws = websocket.WebSocketApp(
            WS_URL,
            header={"Origin": ORIGIN},
            on_message=self.on_message
        )
        self.ws.on_open = lambda ws: ws.send(json.dumps({
            "event": "pusher:subscribe",
            "data": {"auth": "", "channel": symbol}
        }))
        self.ws.run_forever()
