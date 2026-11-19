"""Fetch and cache price data."""
from pathlib import Path

import pandas as pd
import yfinance as yf


def get_prices(ticker, start, end, use_cache=True):
    file_path = Path("data") / f"{ticker}_{start}_{end}.csv"

    if use_cache and file_path.exists():
        prices = pd.read_csv(file_path, index_col=0, parse_dates=True)
        return prices.squeeze("columns")
    else:
        print("downloading")
        data = yf.download(ticker, start=start, end=end)
        prices = data["Close"][ticker]
        if use_cache:
            Path("data").mkdir(exist_ok=True)
            prices.to_csv(file_path)
        return prices