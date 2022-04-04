import pandas as pd
from data_visualization.functions import plot_macd, prepare_data, plot, plot_all
from index_functions.functions import macd, signal, sell_buy_signals, trading_algorythm

amd_data = pd.read_csv('./app/AMD.csv')

prepare_data(amd_data)
macd(amd_data, "Close")
signal(amd_data)
sell_buy_signals(amd_data)

plot(amd_data, "Close", "AMD")
plot_macd(amd_data)
plot_all(amd_data, "Close", "AMD")

print(amd_data)
print(f"profit przy inwestycji długoterminowej (1000 dni): {trading_algorythm(amd_data, (len(amd_data) - 1000, len(amd_data) - 1)):.2f}")
print(f"profit przy inwestycji krótkoterminowej (30 dni): {trading_algorythm(amd_data, (len(amd_data) - 30, len(amd_data) - 1)):.2f}")

# dane dla 700 wstecz
print(f"profit przy inwestycji długoterminowej (1000 dni): {trading_algorythm(amd_data, (len(amd_data) - 1000 - 700, len(amd_data) - 1 - 700)):.2f}")
print(f"profit przy inwestycji krótkoterminowej (30 dni): {trading_algorythm(amd_data, (len(amd_data) - 30 - 700, len(amd_data) - 1 - 700)):.2f}")
