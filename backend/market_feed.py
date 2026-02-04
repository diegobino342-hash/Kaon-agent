import time
import threading

class MarketFeed:
    def __init__(self):
        self.last_tick_time = {}
        self.last_price = {}
        self.state = {}
        self.lock = threading.Lock()

    def update(self, symbol, price, timestamp):
        with self.lock:
            self.last_tick_time[symbol] = timestamp
            self.last_price[symbol] = price
            self.state[symbol] = "LIVE"

    def is_live(self, symbol, max_delay_ms=5000):
        with self.lock:
            ts = self.last_tick_time.get(symbol)
            if not ts:
                return False
            now_ms = int(time.time() * 1000)
            return (now_ms - ts) < max_delay_ms

    def mark_stale(self, symbol):
        with self.lock:
            self.state[symbol] = "STALE"

    def get_state(self, symbol):
        return self.state.get(symbol, "UNKNOWN")
