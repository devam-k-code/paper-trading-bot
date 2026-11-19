"""Runs the bot live separate from the backtesting code."""

from datetime import date, timedelta

from tradebot.data import get_prices
from tradebot.strategy import moving_average_signals


def todays_signal(ticker):
    start = date.today() - timedelta(days=120)
    prices = get_prices(ticker, start, date.today(), use_cache=False)
    signals = moving_average_signals(prices, 20, 50)
    return signals.iloc[-1]