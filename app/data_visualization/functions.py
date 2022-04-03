from pandas import DataFrame
from pandas import to_datetime
import matplotlib.pyplot as plt

# TODO: Wizualizacja dancyh na 1 wykresie

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


def plot_all(df: DataFrame, column: str, company: str, count: int=1000) -> None:
    fig, ax = plt.subplots(nrows=2)

    plot_df = df.tail(count)
    
    plot_df.plot(y=column, ax=ax[0])


    ax[0].set_axisbelow(True)
    ax[0].minorticks_on()

    ax[0].grid(which="major", linestyle="-", linewidth="0.5", color="red")
    ax[0].grid(which="minor", linestyle=":", linewidth="0.5", color="black")

    ax[0].set_title(f"Cena akcji {company}")
    ax[0].set_xlabel("Data")
    ax[0].set_ylabel("Cena zamknięcia [USD]")

    plot_df.plot(y = "MACD", ax=ax[1])
    plot_df.plot(y = "SIGNAL", ax=ax[1])
    ax[1].set_axisbelow(True)
    ax[1].minorticks_on()

    ax[1].grid(which="major", linestyle="-", linewidth="0.5", color="red")
    ax[1].grid(which="minor", linestyle=":", linewidth="0.5", color="black")

    ax[1].set_title(f"Wartości MACD oraz SIGNAL")
    ax[1].set_xlabel("Data")
    ax[1].set_ylabel("MACD")

    fig.tight_layout()

    plt.show()
    
    
def plot_macd(df: DataFrame, count: int=1000) -> None:
    
    _, ax = plt.subplots()

    plot_df = df.tail(count)

    plot_df.plot(y = "MACD", ax=ax)
    plot_df.plot(y = "SIGNAL", ax=ax)
    ax.set_axisbelow(True)
    ax.minorticks_on()

    ax.grid(which="major", linestyle="-", linewidth="0.5", color="red")
    ax.grid(which="minor", linestyle=":", linewidth="0.5", color="black")

    plt.title(f"Wartości MACD oraz SIGNAL")
    plt.xlabel("Data")
    plt.ylabel("MACD")

    plt.show()
