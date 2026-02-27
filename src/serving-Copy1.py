# src/serving.py

import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

# ---------------------------
# Definir API
# ---------------------------
app = FastAPI(title="Diabetes Prediction API")

# ---------------------------
# Clase de entrada
# ---------------------------
class PatientData(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

# ---------------------------
# Cargar modelo y scaler
# ---------------------------
model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")

# ---------------------------
# Endpoint de predicción
# ---------------------------
@app.post("/predict")
def predict(data: PatientData):
    # Convertir datos a DataFrame
    df = pd.DataFrame([data.dict()])
    
    # Escalar datos
    X_scaled = scaler.transform(df)
    
    # Predecir clase
    pred_class = model.predict(X_scaled)[0]
    pred_prob = model.predict_proba(X_scaled)[0][1]
    
    return {
        "prediction": int(pred_class),
        "probability": float(pred_prob)
    }

# ---------------------------
# Endpoint test rápido
# ---------------------------
@app.get("/")
def root():
    return {"message": "Diabetes Prediction API running!"}