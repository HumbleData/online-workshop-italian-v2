import pandas as pd

df_2014 = pd.read_csv("../data/food_training/training_2014.csv", header=1)
df_2015 = pd.read_csv("../data/food_training/training_2015.csv", header=1)
df_2016 = pd.read_csv("../data/food_training/training_2016.csv", header=1)

dfs = [df_2014, df_2015, df_2016]
df = pd.concat(dfs)

df = df.reset_index()
df.index

# Avremmo anche potuto eseguire la concatenazione nel modo seguente:
# df = pd.concat(frames, ignore_index=True)

print('df.reset_index()\ndf.index\n')
display(df.index)