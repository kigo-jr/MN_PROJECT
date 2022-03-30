import pandas as pd
from data_visualization.functions import prepare_data, plot
from index_functions.functions import macd

amd_data = pd.read_csv('./app/AMD.csv')

prepare_data(amd_data)
plot(amd_data, "Close", "AMD", len(amd_data))


print(amd_data)
print(macd(amd_data, 'Close'))
