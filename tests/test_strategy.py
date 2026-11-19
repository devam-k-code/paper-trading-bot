import pandas as pd
from tradebot.strategy import moving_average_signals, momentum_signals

def test_signals():
    prices = pd.Series([1, 2, 3, 4 ,5])
    signals = moving_average_signals(prices, short=2, long=3)
    assert signals.tolist() == [0, 0, 1, 1, 1]


def test_momentum_signals():
    prices = pd.Series([1, 2, 3, 4, 5])
    signals = momentum_signals(prices, lookback=2)
    assert signals.tolist() == [0, 0, 1, 1, 1]