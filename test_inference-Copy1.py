# run_inference.py
import pandas as pd
import requests

# --- Configuración ---
API_URL = "http://127.0.0.1:8000/predict"  # URL de tu API
DATA_PATH = "data/raw/diabetes.csv"        # Ruta a tu CSV
OUTPUT_PATH = "reports/predictions.csv"    # Ruta de salida de las predicciones

# --- Cargar datos ---
df = pd.read_csv(DATA_PATH)
print(f"Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas")

# --- Preparar predicciones ---
predictions = []

for idx, row in df.iterrows():
    # Convertir cada fila a float y enviar como diccionario
    data = {
        "Pregnancies": float(row["Pregnancies"]),
        "Glucose": float(row["Glucose"]),
        "BloodPressure": float(row["BloodPressure"]),
        "SkinThickness": float(row["SkinThickness"]),
        "Insulin": float(row["Insulin"]),
        "BMI": float(row["BMI"]),
        "DiabetesPedigreeFunction": float(row["DiabetesPedigreeFunction"]),
        "Age": float(row["Age"])
    }
    
    try:
        response = requests.post(API_URL, json=data)  # Usar json=data
        response.raise_for_status()  # Lanza error si status code != 200
        prediction = response.json().get("prediction")  # Obtener predicción
        predictions.append(prediction)
    except requests.exceptions.RequestException as e:
        print(f"Error en la fila {idx}: {e}")
        predictions.append(None)

# --- Guardar resultados ---
df["prediction"] = predictions
df.to_csv(OUTPUT_PATH, index=False)
print(f"Predicciones guardadas en: {OUTPUT_PATH}")