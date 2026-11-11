"""Trading strategies that turn prices into signals."""

def moving_average_signals(prices, short, long):
    short_avg = prices.rolling(short).mean()
    long_avg = prices.rolling(long).mean()

    comparison = (short_avg > long_avg).astype(int)
    return comparison