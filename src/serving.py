# src/serving.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import pandas as pd
import joblib

# --- Inicializar app ---
app = FastAPI(title="Diabetes Prediction API")

# --- Cargar modelo entrenado ---
MODEL_PATH = "models/diabetes_model.pkl"
model = joblib.load(MODEL_PATH)

# --- Definir esquema de datos ---
class DiabetesData(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float

class BatchData(BaseModel):
    data: List[DiabetesData]

# --- Endpoint individual (opcional) ---
@app.post("/predict")
def predict(data: DiabetesData):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)[0]
    return {"prediction": int(prediction)}

# --- Endpoint batch ---
@app.post("/predict_batch")
def predict_batch(batch: BatchData):
    try:
        df = pd.DataFrame([item.dict() for item in batch.data])
        predictions = model.predict(df).tolist()
        return {"predictions": [int(p) for p in predictions]}
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))