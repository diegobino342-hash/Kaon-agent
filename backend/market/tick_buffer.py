class TickBuffer:
    def __init__(self):
        self.ticks = []

    def add(self, price, timestamp):
        self.ticks.append((timestamp, price))
