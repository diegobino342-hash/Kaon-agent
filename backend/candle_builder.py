class CandleBuilder:
    def __init__(self):
        self.current = None
        self.candles = []

    def add_tick(self, price, ts):
        bucket = ts // 300000
        if not self.current or self.current["bucket"] != bucket:
            if self.current:
                self.candles.append(self.current)
            self.current = {
                "bucket": bucket,
                "open": price,
                "high": price,
                "low": price,
                "close": price
            }
        else:
            self.current["high"] = max(self.current["high"], price)
            self.current["low"] = min(self.current["low"], price)
            self.current["close"] = price
