import os
from dotenv import load_dotenv

load_dotenv()

PUSHER_APP_KEY = os.getenv("PUSHER_APP_KEY")
PUSHER_HOST = "wss://ws-us2.pusher.com"
ORIGIN = "https://www.homebroker.com"

TIMEFRAME_SECONDS = 60
MIN_PROBABILITY = 0.80
