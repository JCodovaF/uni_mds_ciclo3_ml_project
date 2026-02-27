# src/train.py
import mlflow
import mlflow.sklearn
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score

# ---------------------------
# Cargar dataset limpio
# ---------------------------
df = pd.read_csv("data/features/diabetes_clean.csv")
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ---------------------------
# Entrenar Random Forest
# ---------------------------
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

# Evaluar
y_pred = rf.predict(X_test)
y_prob = rf.predict_proba(X_test)[:, 1]

roc_auc = roc_auc_score(y_test, y_prob)
print(classification_report(y_test, y_pred))
print("ROC-AUC:", roc_auc)

# ---------------------------
# MLflow Tracking
# ---------------------------
mlflow.set_experiment("diabetes_rf_experiment")  # Nombre del experimento

with mlflow.start_run(run_name="rf_champion"):

    # Guardar métricas
    mlflow.log_metric("roc_auc", roc_auc)

    # Guardar modelo
    mlflow.sklearn.log_model(rf, "random_forest_model")

    # Guardar parámetros (opcional)
    mlflow.log_param("random_state", 42)
    mlflow.log_param("n_estimators", rf.n_estimators)

print("✅ Modelo registrado en MLflow")