def decide(df):
    last = df.iloc[-1]

    if last["rsi"] < 30 and last["close"] < last["bb_low"]:
        return "CALL", 83

    if last["rsi"] > 70 and last["close"] > last["bb_high"]:
        return "PUT", 82

    return None
