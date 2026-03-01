# MLOps Introduction: Final Project

Student info:
- Full name: Jorge Arturo Córdova Fernández
- e-mail: jorge.cordova.f@uni.pe
- Grupo: Grupo 2

## Project Name: Algoritmo para la predicción de la diabetes

## 📄 Descripción
El objetivo de este proyecto es predecir si una persona padece diabetes o no usando el dataset clásico de Pima Indians Diabetes.
Para ello se construye un pipeline completo de Machine Learning Operations (MLOps) que incluye:
Preparación de datos
Entrenamiento y evaluación de modelos
Selección de modelo campeón
Despliegue del modelo mediante API REST
Generación de inferencias y reportes
Este flujo, automatizado y reproducible, permite llevar un modelo desde la experimentación hasta un servicio de inferencia utilizable en producción.

📊 2. Dataset
📍 Origen
El dataset utilizado es el “Pima Indians Diabetes Dataset”, muy popular en la literatura de clasificación binaria para diagnóstico médico.

🧾 Descripción de variables
El dataset contiene registros de pacientes con características médicas y una etiqueta binaria que indica si tienen diabetes (1) o no (0).
Ejemplos de features incluidos:
Variable	Tipo	Descripción
Pregnancies	Numérica	Número de embarazos
Glucose	Numérica	Nivel de glucosa en sangre
BloodPressure	Numérica	Presión arterial
SkinThickness	Numérica	Grosor de piel
Insulin	Numérica	Nivel de insulina
BMI	Numérica	Índice de masa corporal
DiabetesPedigreeFn	Numérica	Función de historial genético
Age	Numérica	Edad
Outcome	Binaria	1 = diabetes, 0 = no diabetes (label)

🧪 Exploración y preparación de datos
La preparación de datos es realizada en src/data_preparation.py. Incluye:
Lectura de data/raw/diabetes.csv
Limpieza y revisión de valores faltantes
Transformación/normalización de features
Guardado de datos procesados en data/processed/
Estas etapas aseguran que los modelos reciban datos consistentes y comparables para entrenar y evaluar.

🤖 Modelos y Experimentación
El script src/train.py entrena y evalúa varios modelos supervisados:
📌 Modelos evaluados
Logistic Regression
Random Forest Classifier
Se usan las métricas clásicos de clasificación:
Accuracy
F1-score
Matriz de confusión

📊 Resultados registrados:
Logistic Regression: Accuracy ~0.78
Random Forest: Accuracy ~0.81 (Modelo campeón)
Random Forest fue seleccionado como modelo final por tener mejores métricas generalizadas según validación.

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
data/raw/diabetes.csv → Dataset original.<br>
src/data_preparation.py → Limpieza, manejo de valores nulos, transformación de columnas.

2️⃣ Entrenamiento de modelos
src/train.py → Entrena varios modelos (Logistic Regression, Random Forest, etc.).<br>
models/ → Carpeta donde se guardan los modelos entrenados (.pkl o .joblib).<br>
Evaluación de modelos → Determina el modelo “champion” según métricas (accuracy, f1-score, etc.).<br>
Opcional: MLflow para tracking de experimentos (si estuviera instalado).

3️⃣ API / Model Serving
src/serving.py → API con FastAPI para servir el modelo campeón.<br>
Endpoints:<br>
/predict → Recibe un solo registro y devuelve una predicción.<br>
/predict_batch → Recibe múltiples registros y devuelve predicciones.<br>

4️⃣ Inferencia y Reportes
El script test_inference.py automatiza la generación de predicciones:
Carga un dataset de prueba
Llama al endpoint /predict
Guarda las predicciones en reports/predictions.csv
Genera reportes y matrices de confusión
Esto facilita comparaciones y análisis cuantitativo de desempeño fuera del proceso de entrenamiento.

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

