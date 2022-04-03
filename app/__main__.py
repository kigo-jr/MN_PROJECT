import pandas as pd
from data_visualization.functions import plot_macd, prepare_data, plot, plot_all
from index_functions.functions import macd, signal

amd_data = pd.read_csv('./app/AMD.csv')

prepare_data(amd_data)
macd(amd_data, "Close")
signal(amd_data)

plot(amd_data, "Close", "AMD")
plot_macd(amd_data)
plot_all(amd_data, "Close", "AMD")

print(amd_data)
