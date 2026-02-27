# test_inference_batch.py
import pandas as pd
import requests
import json
from pathlib import Path

# --- Configuración ---
API_URL = "http://127.0.0.1:8000/predict_batch"
DATA_PATH = Path("data/raw/diabetes.csv")
REPORTS_PATH = Path("reports/predictions.csv")

# --- Cargar datos ---
df = pd.read_csv(DATA_PATH)
print(f"Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas")

# --- Preparar payload para batch ---
payload = {"data": df.to_dict(orient="records")}

# --- Llamar API ---
try:
    response = requests.post(API_URL, json=payload)
    response.raise_for_status()
    predictions = response.json()["predictions"]
    print(f"Predicciones recibidas: {len(predictions)}")

    # --- Guardar resultados ---
    df["prediction"] = predictions
    REPORTS_PATH.parent.mkdir(exist_ok=True)
    df.to_csv(REPORTS_PATH, index=False)
    print(f"Predicciones guardadas en {REPORTS_PATH}")

except requests.exceptions.RequestException as e:
    print(f"Error al conectarse al API: {e}")