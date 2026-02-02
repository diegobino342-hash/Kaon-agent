import time

class CandleBuilder:
    def __init__(self):
        self.candles = []

    def add_tick(self, price, timestamp):
        minute = timestamp // 60000
        if not self.candles or self.candles[-1]["minute"] != minute:
            self.candles.append({
                "minute": minute,
                "open": price,
                "high": price,
                "low": price,
                "close": price
            })
        else:
            c = self.candles[-1]
            c["high"] = max(c["high"], price)
            c["low"] = min(c["low"], price)
            c["close"] = price

    def get(self):
        return self.candles[-50:]
