import matplotlib.pyplot as plt

from tradebot.data import get_prices
from tradebot.strategy import moving_average_signals
from tradebot.backtest import backtest

prices = get_prices("AAPL", '2020-01-01', '2026-01-01')
signals = moving_average_signals(prices, 20, 50)
equity = backtest(prices, signals)

print(equity.tail())