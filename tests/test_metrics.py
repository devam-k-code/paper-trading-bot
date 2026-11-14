from tradebot.metrics import total_return

import pandas as pd

def test_total_return():
    equity_curve = pd.Series([1,2,3])
    result = total_return(equity_curve)
    assert result == 2