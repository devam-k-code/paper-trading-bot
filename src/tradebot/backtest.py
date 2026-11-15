"""Simulate a strategy over historical prices."""

def backtest(prices, signals):
    daily_returns = prices.pct_change()
    positions = signals.shift(1)
    strategy_returns = daily_returns * positions
    strategy_returns = strategy_returns.fillna(0)
    equity = (1 + strategy_returns).cumprod()
    return equity