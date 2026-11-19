"""Connects to Alpaca API and checks account to place orders."""

import os

from alpaca.trading.client import TradingClient
from dotenv import load_dotenv


def get_client():
    load_dotenv()
    api_key = os.getenv("ALPACA_API_KEY")
    secret_key = os.getenv("ALPACA_SECRET_KEY")
    return TradingClient(api_key, secret_key, paper=True)