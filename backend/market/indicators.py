import numpy as np

def rsi(closes, period=14):
    if len(closes) < period:
        return None
    deltas = np.diff(closes)
    gains = deltas[deltas > 0].sum() / period
    losses = -deltas[deltas < 0].sum() / period
    if losses == 0:
        return 100
    rs = gains / losses
    return 100 - (100 / (1 + rs))
