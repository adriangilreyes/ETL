import pandas as pd

#carga del dataset dengue

def load_data(path="C:/Users/Usuario/Desktop/ProyectosPython/Kaggle-streamlit-dashboard/dengue.csv"):
    df = pd.read_csv(path)
    return df

carga_dataset = load_data()
print(carga_dataset)  

#Inspección
print(carga_dataset.head())
print('-----------------------------------------------') 
print(carga_dataset.info())
print('-----------------------------------------------')
print(carga_dataset.columns)