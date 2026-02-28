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

uni_mds_ciclo3_ml_project/
│
├── data/
│ ├── raw/ # Datos originales
│ └── processed/ # Datos transformados para entrenamiento
│
├── src/
│ ├── data_preparation.py # Limpieza y transformación de datos
│ ├── train.py # Entrenamiento y evaluación de modelos
│ ├── serving.py # API para servir modelo con FastAPI
│ └── run_api.py # Script para ejecutar la API
│
├── notebooks/ # Notebooks de experimentación
├── reports/ # Gráficos, matrices de confusión y reportes
├── test_inference.py # Prueba de la API para generar predicciones
└── README.md


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

