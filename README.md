# MLOps Introduction: Final Project

Student info:
- Full name: Jorge Arturo Córdova Fernández
- e-mail: jorge.cordova.f@uni.pe
- Grupo: Grupo 2

## Project Name: Algoritmo para la predicción de la diabetes

## 📄 Descripción
Este proyecto tiene como objetivo **predecir diabetes** utilizando un dataset clásico de Pima Indians Diabetes y aplicar técnicas de Machine Learning para:
- Preparación de datos.
- Entrenamiento y evaluación de modelos.
- Selección del modelo campeón.
- Despliegue y generación de predicciones vía API REST.

Se realizaron experimentos con **Logistic Regression** y **Random Forest**, evaluando su desempeño con métricas como **accuracy**, **F1-score** y **matriz de confusión**.

---

## 🗂 Estructura del proyecto

uni_mds_ciclo3_ml_project/<br>
│<br>
├── data/<br>
│ ├── raw/ # Datos originales/<br>
│ └── processed/ # Datos transformados para entrenamiento/<br>
│<br>
├── src/<br>
│ ├── data_preparation.py # Limpieza y transformación de datos/<br>
│ ├── train.py # Entrenamiento y evaluación de modelos/<br>
│ ├── serving.py # API para servir modelo con FastAPI/<br>
│ └── run_api.py # Script para ejecutar la API/<br>
│<br>
├── notebooks/ # Notebooks de experimentación/<br>
├── reports/ # Gráficos, matrices de confusión y reportes/<br>
├── test_inference.py # Prueba de la API para generar predicciones/<br>
└── README.md

## 📄 Flujo completo del proyecto MLops

1️⃣ Data
data/raw/diabetes.csv → Dataset original.
src/data_preparation.py → Limpieza, manejo de valores nulos, transformación de columnas.

2️⃣ Entrenamiento de modelos
src/train.py → Entrena varios modelos (Logistic Regression, Random Forest, etc.).
models/ → Carpeta donde se guardan los modelos entrenados (.pkl o .joblib).
Evaluación de modelos → Determina el modelo “champion” según métricas (accuracy, f1-score, etc.).
Opcional: MLflow para tracking de experimentos (si estuviera instalado).

3️⃣ API / Model Serving
src/serving.py → API con FastAPI para servir el modelo campeón.
Endpoints:
/predict → Recibe un solo registro y devuelve predicción.
/predict_batch → Recibe un batch y devuelve predicciones para todos.

4️⃣ Inferencia
test_inference.py → Prueba todo el CSV de entrada y guarda reports/predictions.csv.

5️⃣ Reportes
reports/ → Carpeta con:
Resultados de predicciones (predictions.csv).
Gráficos, métricas, matrices de confusión.

README.md con resumen de experimentos.
---

## ⚙️ Instrucciones de uso

### 1. Preparar datos
python src/data_preparation.py
Este script carga data/raw/diabetes.csv.
Realiza limpieza, reemplazo de valores nulos y guarda los datos procesados en data/processed/

### 2. Entrenar modelos
python src/train.py
Entrena Logistic Regression y Random Forest.
Evalúa desempeño y selecciona el modelo campeón.
Guarda el modelo entrenado en models/.

### 3. Ejecutar API
python src/run_api.py
Inicia un servidor FastAPI en http://127.0.0.1:8000.
Endpoint principal: /predict.

### 4. Generar predicciones
python test_inference.py
Envía datos de prueba al endpoint /predict.
Guarda predicciones en reports/predictions.csv.

📊 Resultados

Accuracy y F1-score:
Logistic Regression: 0.78
Random Forest: 0.81 ✅ Modelo campeón
Matriz de confusión:
Predicciones de ejemplo:
Guardadas en reports/predictions.csv.

📝 Notas adicionales
Todos los scripts deben ejecutarse desde la raíz del proyecto.
Las dependencias principales están en requirements.txt:

pandas
numpy
scikit-learn
fastapi
uvicorn
requests

Para instalar dependencias:
pip install -r requirements.txt

🔗 Enlaces útiles

Notebooks: notebooks/
Reportes: reports/
API FastAPI: /predict para inferencias.

