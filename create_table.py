import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def grafics(df: pd):
    df["Number"] = pd.to_datetime(df["Number"], format="%Y-%m-%d")
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(50, 5))

    axes[0].bar(df["Number"], df["Day temperature"], color="#5900A6")
  #  axes[0].legend(loc=1, prop={'size': 20}) 
    axes[0].set(title='Day temperature')
    axes[0].set_xlabel('date')
    axes[0].set_ylabel("temp")
   # axes[0].set(xticks="date", yticks="temp")

    axes[1].bar(df["Number"], df["Night temperature"], color="#5900A6")
   # axes[1].legend(loc=2, prop={'size': 20}) 
    axes[1].set(title='Night temperature')
    axes[1].set_xlabel('date')
    axes[1].set_ylabel("temp")

   # plt.title("Temperature")

    plt.show()


def grafics_date(df: pd, month: int, year: int):
    fig = plt.figure(figsize=(40, 5))
    plt.ylabel("temp")
    plt.xlabel("date")
    plt.title("Temperature")
    tmp_df = df.loc[(df["Number"].dt.year == year) & (df["Number"].dt.month == month)]
    plt.bar(tmp_df["Number"], tmp_df["Day temperature"], color="#5900A6")
    plt.show()


def temperature_filter(df: pd, temp: float):
    # df[df['height'] > 175
    return df[df["Day temperature"] >= temp]


def number_filter(df: pd, start: str, end: str):
    df["Number"] = pd.to_datetime(df["Number"], format="%Y-%m-%d")
    return df.loc[(df["Number"] >= start) & (df["Number"] <= end)]
    # return df[df["Number"] >= start]  # [df["Numer"]<=end]


def groupby_date(df: pd):
    df["Number"] = pd.to_datetime(df["Number"], format="%Y-%m-%d")
    return df.groupby(df["Number"].dt.month)[
        "Day temperature",
        "Night temperature",
        "Fahrenheit (afternoon)",
        "Fahrenheit (night)",
    ].mean()


def statistics(df: pd) -> None:
    print(
        df["Day temperature"].describe(),
        df["Night temperature"].describe(),
        df["Fahrenheit (afternoon)"].describe(),
        df["Fahrenheit (night)"].describe(),
    )


def datafrem() -> pd:
    df = pd.read_csv("dataset.csv", sep=",")
    # print(df.describe())
    df["Number"] = pd.to_datetime(df["Number"], format="%Y-%m-%d")
    df["Fahrenheit (afternoon)"] = df["Day temperature"] * 1.8 + 32
    df["Fahrenheit (night)"] = df["Night temperature"] * 1.8 + 32

    return df


# print(df.loc[2800])


if __name__ == "__main__":
    df = datafrem()
    start = "2020-10-08"
    end = "2021-11-17"
    # print(df)
    # print(number_filter(df, start, end))
    # print(groupby_date(df))
    grafics(df)
    #grafics_date(df, 11, 2012)
# print(df.loc[2800])
# temperature_filter(df, 21)
# statistics(df)
