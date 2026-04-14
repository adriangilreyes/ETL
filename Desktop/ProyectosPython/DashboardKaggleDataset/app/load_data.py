import pandas as pd

df = pd.read_csv("C:/Users/Usuario/Downloads/archive/Dengue.csv")

def dataset_load():
    return df

#imprimir dataset (Dengue.csv)
print(dataset_load())

print(df.head(34))
print(df.describe())
print(df.tail(34))

