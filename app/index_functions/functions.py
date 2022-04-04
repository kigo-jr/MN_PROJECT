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

    return_df["MACD"] = return_df["EMA_26"] - return_df["EMA_12"]

    return return_df


def signal(df: DataFrame, inplace: bool=True) -> DataFrame:
    return_df = df
    if not inplace:
        return_df = df.copy()
    
    return_df["SIGNAL"] = ema(9, return_df, "MACD", False)['EMA_9']

    return return_df

def sell_buy_signals(df: DataFrame, inplace: bool=True):
    pass
    