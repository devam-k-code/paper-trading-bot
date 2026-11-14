import pandas as pd
import pytest
from tradebot.metrics import total_return, max_drawdown


def test_total_return():
    equity_curve = pd.Series([1, 2, 3])
    result = total_return(equity_curve)
    assert result == 2

def test_max_drawdown():
    equity = pd.Series([1.0, 1.5, 1.2, 1.6, 1.1])
    output = max_drawdown(equity)
    assert output == -0.3125