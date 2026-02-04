import websocket
import json
import threading

DERIV_WS = "wss://ws.binaryws.com/websockets/v3?app_id=1089"

class MarketSocket:
    def __init__(self):
        self.url = DERIV_WS
        self.ws = None

    # ===============================
    # MÉTODO QUE ESTAVA FALTANDO
    # ===============================
    def connect(self, _=None):
        """
        Método de compatibilidade.
        NÃO muda arquitetura.
        Apenas inicia o WebSocket corretamente.
        """

        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )

        # Rodar em thread para não travar o processo
        threading.Thread(
            target=self.ws.run_forever,
            daemon=True
        ).start()

    # ===============================
    # CALLBACKS
    # ===============================
    def on_open(self, ws):
        print("[WS] Conectado à Deriv")

        # Exemplo de subscribe (mantém estrutura aberta)
        ws.send(json.dumps({
            "ticks": "frxEURUSD"
        }))

    def on_message(self, ws, message):
        data = json.loads(message)

        if "tick" in data:
            price = data["tick"]["quote"]
            epoch = data["tick"]["epoch"]
            # Aqui entra sua lógica real (inalterada)
            # print(f"[TICK] {price} @ {epoch}")

    def on_error(self, ws, error):
        print("[WS ERROR]", error)

    def on_close(self, ws, *_):
        print("[WS] Conexão encerrada")
