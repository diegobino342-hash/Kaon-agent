import math

class CandleBuilder:
    def __init__(self, timeframe=60):
        self.timeframe = timeframe
        self.current = None

    def add_tick(self, timestamp, price):
        bucket = math.floor(timestamp / 1000 / self.timeframe) * self.timeframe
        if not self.current or self.current["time"] != bucket:
            self.current = {
                "time": bucket,
                "open": price,
                "high": price,
                "low": price,
                "close": price
            }
            return self.current
        self.current["high"] = max(self.current["high"], price)
        self.current["low"] = min(self.current["low"], price)
        self.current["close"] = price
        return None
