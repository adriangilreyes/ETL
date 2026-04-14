from load_data import load_data
import pandas as pd

#cargamos el dataset
df = pd.read_csv("C:/Users/Usuario/Desktop/ProyectosPython/Kaggle-streamlit-dashboard/dengue.csv")

def clean_data(df):
    df.columns = df.columns.str.strip().str.lower()
    df = df.dropna()
    return df

clean = clean_data(df)
print(clean)  