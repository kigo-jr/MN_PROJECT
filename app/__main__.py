import pandas as pd
from data_visualization.functions import prepare_data, plot, plot_macd
from index_functions.functions import macd, ema, signal

amd_data = pd.read_csv('./app/AMD.csv')

prepare_data(amd_data)
plot(amd_data, "Close", "AMD", len(amd_data))

macd(amd_data, "Close")
signal(amd_data)

plot_macd(amd_data, "AMD", len(amd_data))
print(amd_data)
