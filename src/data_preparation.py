# src/data_preparation.py

import pandas as pd
import os

def load_data(path="data/raw/diabetes.csv"):
    """
    Cargar dataset de diabetes.
    Usa header=0 porque el CSV ya tiene nombres de columnas.
    """
    df = pd.read_csv(path, header=0)
    return df

def clean_data(df):
    """
    Limpiar datos: reemplazar ceros por mediana en columnas específicas.
    """
    cols_with_zero = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    df[cols_with_zero] = df[cols_with_zero].replace(0, pd.NA)
    df.fillna(df.median(), inplace=True)
    return df

def save_clean_data(df, path="data/features/diabetes_clean.csv"):
    """
    Guardar dataset limpio en carpeta features.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"✅ Dataset limpio guardado en: {path}")

if __name__ == "__main__":
    # Cargar, limpiar y guardar dataset
    df = load_data()
    df = clean_data(df)
    save_clean_data(df)