from websocket_client import MarketSocket
from candle_builder import CandleBuilder
from indicators import apply
from decision_engine import decide
from config import SYMBOL

builder = CandleBuilder()
latest_signal = {}

def on_tick(tick):
    global latest_signal

    builder.add_tick(tick["price"], tick["timestamp"])

    # LOG PARA CONFIRMAR VIDA
    print("TICK:", tick["price"])

    if len(builder.candles) < 20:
        return

    df = apply(builder.candles)
    decision = decide(df)

    if decision:
        direction, prob = decision
        latest_signal = {
            "symbol": SYMBOL,
            "direction": direction,
            "probability": prob
        }
        print("SINAL GERADO:", latest_signal)

def start():
    ws = MarketSocket(on_tick)
    ws.start(SYMBOL)

def get_signal():
    return latest_signal

def get_candles():
    return builder.get_candles()
