"""Performance metrics: returns, Sharpe ratio, drawdown."""
def total_return(equity):
    return equity.iloc[-1] / equity.iloc[0] - 1