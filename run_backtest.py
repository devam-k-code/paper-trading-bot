import matplotlib.pyplot as plt

from tradebot.data import get_prices
from tradebot.strategy import moving_average_signals
from tradebot.backtest import backtest
from tradebot.metrics import total_return, max_drawdown, sharpe_ratio

prices = get_prices("AAPL", '2020-01-01', '2026-01-01')
signals = moving_average_signals(prices, 20, 50)
equity = backtest(prices, signals)

buy_hold = prices / prices.iloc[0]

print(f"Strategy  return: {total_return(equity):.2f}  drawdown: {max_drawdown(equity):.2f}  sharpe: {sharpe_ratio(equity):.2f}")
print(f"Buy and Hold  return: {total_return(buy_hold):.2f}  drawdown: {max_drawdown(buy_hold):.2f}  sharpe: {sharpe_ratio(buy_hold):.2f}")
