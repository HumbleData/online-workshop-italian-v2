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

paese_in_codici = df["country"].isin(diz_codici.keys())
df.loc[paese_in_codici, "country"] = df.loc[paese_in_codici, "country"].map(diz_codici)

print('df.loc[df["city"] == "unknown", "country"]\n')

display(df.loc[df["city"] == "unknown", "country"])