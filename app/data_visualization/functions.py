from pandas import DataFrame
from pandas import to_datetime
import matplotlib.pyplot as plt

def prepare_data(df: DataFrame) -> None:
    df["Date"] = to_datetime(df["Date"], format="%Y-%m-%d")
    df.set_index(["Date"], inplace=True)


def plot(df: DataFrame, column: str, company: str, count: int=1000) -> None:
    _, ax = plt.subplots()

    plot_df = df.tail(count)
    
    plot_df.plot(y=column, ax=ax)


    ax.set_axisbelow(True)
    ax.minorticks_on()

    ax.grid(which="major", linestyle="-", linewidth="0.5", color="red")
    ax.grid(which="minor", linestyle=":", linewidth="0.5", color="black")

    plt.title(f"Cena akcji {company}")
    plt.xlabel("Data")
    plt.ylabel("Cena zamknięcia [USD]")

    plt.show()

def plot_macd(df: DataFrame, company: str, count: int=1000) -> None:
    
    _, ax = plt.subplots()

    plot_df = df.tail(count)

    plot_df.plot(y = "MACD", ax=ax)
    plot_df.plot(y = "SIGNAL", ax=ax)
    ax.set_axisbelow(True)
    ax.minorticks_on()

    ax.grid(which="major", linestyle="-", linewidth="0.5", color="red")
    ax.grid(which="minor", linestyle=":", linewidth="0.5", color="black")

    plt.title(f"Cena akcji {company}")
    plt.xlabel("Data")
    plt.ylabel("MACD")

    plt.show()
    