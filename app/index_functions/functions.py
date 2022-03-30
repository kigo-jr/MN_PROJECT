import numpy
from pandas import DataFrame


def ema(span: int, df: DataFrame, column: str) -> DataFrame:
    return_df = df

    alpha = 2 / (span + 1)

    

    return return_df


def macd(df: DataFrame, column: str) -> DataFrame:
    return_df = df

    return_df['EMA_12'] = ema(12, return_df, column)
    return_df['EMA_26'] = ema(26, return_df, column)
    return_df['MACD'] = return_df['EMA_26'].subtract(return_df['EMA_12'])

    return df


    