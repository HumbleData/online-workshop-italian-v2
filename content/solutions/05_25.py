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

print('df["city"][df["city"].str.contains("/")]\n')

display(df["city"][df["city"].str.contains("/")])