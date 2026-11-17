# Paper Trading Bot

This is a learning project.


This code is a Python backtester for simple trading strategies on US stocks. It downloads daily prices, turns them into buy/sell signals, simulates the strategy, and compares it against just buying and holding.

The long-term goal is to run the same strategies live on an Alpaca paper trading account.

## Results

20/50-day moving average crossover on AAPL, January 2020 to December 2025 (1,508 trading days):

![Backtest](backtest.png)

| Metric | MA crossover | Buy and hold |
|---|---|---|
| Total return | +116.5% | +275.1% |
| Max drawdown | -29.1% | -33.4% |
| Sharpe ratio | 0.74 | 0.85 |

## What I found

The strategy makes money, but less than half of what buy and hold made. AAPL went up a lot over this period, and the strategy spent a big part of it in cash. Moving averages only cross after a trend has already started, so it buys late and sells late.

It did have a smaller worst drop (-29% vs -33%). The Sharpe ratio islower, so it didn't make up for the lost return by taking less risk.

## How it works

- `data.py` downloads daily closing prices with yfinance and caches them as CSV files in `data/`
- `strategy.py` holds the stock (1) when the 20-day average is above the 50-day average, otherwise stays in cash (0)
- `backtest.py` uses the previous day's signal for each day's return, so the strategy can't see the future
- `metrics.py` calculates total return, max drawdown and annualized Sharpe ratio

## Running it

Needs **Python 3.10** or newer.

```
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux
pip install -e ".[dev]"
```

Run the backtest (prints the metrics and saves `backtest.png`):

```
python run_backtest.py
```

Run the tests:

```
pytest
```

## Next steps to finish the project

- More tests, including one that checks the backtest doesn't use future data
- Transaction costs
- More strategies (momentum, RSI) and testing on other tickers
- Live paper trading with the Alpaca API
