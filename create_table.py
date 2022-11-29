import pandas as pd

def filter_of_tepruch(df: pd, temp: float):
    df[df["Температура днем"]]>temp
    print(df)

def statistics(df: pd) -> None:
    print(
        df["Температура днем"].describe(),
        df["Температура ночью"].describe(),
        df["Фарингейт (днем)"].describe(),
        df["Фарингейт (ночью)"].describe(),
    )


def datafrem() -> pd:
    #  name_df = pd.DataFrame({"Число", "Температура днем", "Давление днем", "Ветер днем", "Температура ночью", "Давление ночью", "Ветер ночью"})
    df = pd.read_csv("dataset.csv", sep=",")
    # print(df.describe())
    df["Фарингейт (днем)"] = df["Температура днем"] * 1.8 + 32
    df["Фарингейт (ночью)"] = df["Температура ночью"] * 1.8 + 32
    df.fillna(
        {
            "Температура днем": "данные отсутствуют",
            "Давление днем": "данные отсутствуют",
            "Ветер днем": "данные отсутствуют",
            "Температура ночью": "данные отсутствуют",
            "Давление ночью": "данные отсутствуют",
            "Ветер ночью": "данные отсутствуют",
            "Фарингейт (днем)": "данные отсутствуют",
            "Фарингейт (ночью)": "данные отсутствуют",
        },
        inplace=True,
    )
    return df


# print(df.loc[2800])


if __name__ == "__main__":
    df=datafrem()
   # print(df)
   # print(df.loc[2800])
    filter_of_tepruch(df, 20)
    #statistics(df)
