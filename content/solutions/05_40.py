import pandas as pd

df_2014 = pd.read_csv("../data/food_training/training_2014.csv", header=1)
df_2015 = pd.read_csv("../data/food_training/training_2015.csv", header=1)
df_2016 = pd.read_csv("../data/food_training/training_2016.csv", header=1)

dfs = [df_2014, df_2015, df_2016]
df = pd.concat(dfs)

df = df.reset_index()
df.index

colonne_da_rimuovere = ["Unnamed: 5", "Unnamed: 6"]
df = df.drop(colonne_da_rimuovere, axis=1)

df[["city", "country"]] = df["Location"].str.split(pat=";", expand=True)

df = df.drop("Location", axis=1)

df["city"] = df["city"].str.lower()

df["city"] = df["city"].str.replace(r"/\w*", "", regex=True)

diz_codici = {'BG':'Bulgaria',
              'CZ':'Czech Republic',
              'IT':'Italy',
              'GR':'Greece',
              'SI':'Slovenia',
              'UK':'United Kingdom'}

città_sconosciuta = df["city"] == "unknown"
df.loc[città_sconosciuta, "city"] = df.loc[città_sconosciuta, "country"].map(diz_codici)

city_diz = df.loc[df['country'].notnull(), ['city', 'country']].set_index('city').to_dict()['country']

city_diz.update(
    {
        "bristol": "United Kingdom",
        "gothenburg": "Sweden",
        "graz": "Austria",
        "lyon": "France",
        "murcia": "Spain",
        "parma": "Italy",
    },
)

paese_null = df["country"].isnull()
df.loc[paese_null, "country"] = df.loc[paese_null, "city"].map(city_diz)

df["country"].value_counts(dropna=False)


def f(x):
    if x == 1:
        return "single"
    else:
        return "multiple"

df["Attendees"].apply(f)


languages = pd.read_csv("../data/food_training/languages.csv")

df = df.merge(languages, how="left", left_on="country", right_on="Country")

df = df.drop("Country", axis=1)

print('df["DateFrom"] = pd.to_datetime(df["DateFrom"], format="%Y-%m-%d")\n')
print('df["DateTo"] = pd.to_datetime(df["DateTo"], format="%Y-%m-%d")')

df["DateFrom"] = pd.to_datetime(df["DateFrom"], format="%Y-%m-%d")
df["DateTo"] = pd.to_datetime(df["DateTo"], format="%Y-%m-%d")