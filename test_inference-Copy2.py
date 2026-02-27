# test_inference.py
import pandas as pd
import requests
import os

# --- Configuración ---
DATA_PATH = "data/raw/diabetes.csv"
REPORTS_DIR = "reports"
API_URL = "http://127.0.0.1:8000/predict_batch"  # endpoint batch

# Crear carpeta reports si no existe
os.makedirs(REPORTS_DIR, exist_ok=True)

# --- Cargar datos ---
col_names = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", 
             "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"]

df = pd.read_csv(DATA_PATH, names=col_names, header=0)
print(f"Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas")

# --- Preparar los datos (sin la columna target) ---
data_list = df.drop("Outcome", axis=1).to_dict(orient="records")

# --- Enviar al API en batch ---
try:
    response = requests.post(API_URL, json={"data": data_list})
    response.raise_for_status()
    predictions = response.json()["predictions"]
except requests.exceptions.RequestException as e:
    print("Error al llamar a la API:", e)
    predictions = [None] * len(df)

# --- Guardar resultados ---
df["prediction"] = predictions
output_path = os.path.join(REPORTS_DIR, "predictions_batch.csv")
df.to_csv(output_path, index=False)
print(f"Predicciones guardadas en: {output_path}")