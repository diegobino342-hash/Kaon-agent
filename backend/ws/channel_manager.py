class ChannelManager:
    def __init__(self, ws):
        self.ws = ws
        self.current_channel = None

    def subscribe(self, symbol):
        if self.current_channel:
            self.unsubscribe(self.current_channel)
        self.current_channel = symbol
        self.ws.send({
            "event": "pusher:subscribe",
            "data": {"auth": "", "channel": symbol}
        })

    def unsubscribe(self, symbol):
        self.ws.send({
            "event": "pusher:unsubscribe",
            "data": {"channel": symbol}
        })
