from analysis.indicators import apply_indicators

class DecisionEngine:
    def analyze(self, asset, candles):
        df = apply_indicators(candles)
        last = df.iloc[-1]

        if last["rsi"] < 30:
            return {"asset": asset, "action": "CALL", "prob": 0.82}
        if last["rsi"] > 70:
            return {"asset": asset, "action": "PUT", "prob": 0.81}

        return None
