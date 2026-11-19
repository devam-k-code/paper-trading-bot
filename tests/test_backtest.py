import pandas as pd
from tradebot.backtest import backtest

def test_no_look_ahead():
    prices = pd.Series([100, 100, 110])
    signals = pd.Series([0, 0, 1])
    equity = backtest(prices, signals)
    assert equity.iloc[-1] == 1.0