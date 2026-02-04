import time
from market_socket import MarketSocket

class TradingAgent:
    def __init__(self):
        # instância correta do socket
        self.ws = MarketSocket()

    def start(self):
        # chamada correta do método existente
        self.ws.connect()

        # manter o processo vivo (necessário no Render)
        while True:
            time.sleep(1)
