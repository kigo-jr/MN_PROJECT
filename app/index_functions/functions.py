from typing import Tuple
import numpy as np
from pandas import DataFrame


def ema(span: int, df: DataFrame, column: str, inplace: bool=True) -> DataFrame:
    
    return_df = df
    if not inplace:
        return_df = df.copy()
    
    data = list(return_df[column])
    ema = [np.nan for i in range(len(df))]
    smoothing_factor = 2 / (span + 1)

    for i in range(len(return_df) - 1, span+1, -1):
        num = .0
        den = .0
        for j in range(span):
            num += ((1 - smoothing_factor) ** j) * data[i - j]
            den += (1 - smoothing_factor) ** j
        ema[i] = num/den

    return_df[f"EMA_{span}"] = ema

    return return_df


def macd(df: DataFrame, column: str, inplace: bool=True) -> DataFrame:
    
    return_df = df
    if not inplace:
        return_df = df.copy()

    ema(12, return_df, column)
    ema(26, return_df, column)

    return_df["MACD"] = return_df["EMA_12"] - return_df["EMA_26"]

    return return_df


def signal(df: DataFrame, inplace: bool=True) -> DataFrame:
    return_df = df
    if not inplace:
        return_df = df.copy()
    
    return_df["SIGNAL"] = ema(9, return_df, "MACD", False)['EMA_9']

    return return_df


def sell_buy_signals(df: DataFrame, inplace: bool=True):

    return_df = df
    if not inplace:
        return_df = df.copy()

    diff = list(return_df["MACD"] - return_df["SIGNAL"])
    
    choice = [np.nan for i in range(len(return_df))]

    for i in range(1, len(diff)):
        if diff[i] != np.nan and diff[i] > 0 and diff[i-1] < 0:
            choice[i] = "buy"
        elif diff[i] != np.nan and diff[i] < 0 and diff[i-1] > 0:
            choice[i] = "sell"

    return_df["CHOICE"] = choice

    return return_df


def trading_algorythm(df: DataFrame, period: Tuple[int, int] )-> int:
    bs_data = list(df["CHOICE"])[min(period):max(period)+1]  # buy/sell data ofc
    stock_prices = list(df["Close"])[min(period):max(period)+1]
    
    units = 1000
    money = 0

    for i in range(max(period) - min(period)):
        if bs_data[i] == "buy" and money > 0:
            units += money / stock_prices[i] # za ca??e dost??pne pieni??dze kupujemy tyle akcji ile to mo??liwe
            money = 0
        if bs_data[i] == "sell" and units > 0:
            money = units * stock_prices[i] #  sprzedajemy wszystko
            units = 0

    profit = (units * stock_prices[-1] + money) / (1000*stock_prices[0])
    
    return profit
