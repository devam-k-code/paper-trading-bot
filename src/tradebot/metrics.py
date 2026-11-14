"""Performance metrics: returns, Sharpe ratio, drawdown."""
import math

def total_return(equity):
    return equity.iloc[-1] / equity.iloc[0] - 1


def max_drawdown(equity):
    peak = equity.cummax()
    drawdown = equity / peak -1 
    return drawdown.min()


def sharpe_ratio(equity):
    daily_returns = equity.pct_change()
    mean = daily_returns.mean()
    standard_deviation = daily_returns.std()
    daily_sharpe_ratio = mean / standard_deviation
    yearly_number = daily_sharpe_ratio * math.sqrt(252)
    return yearly_number