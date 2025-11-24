# app_dashboard/services/ml_service.py
import joblib
import numpy as np
import os

MODELO_PATH = "models/modelo_rf.pkl"

class ModeloNaoTreinadoError(Exception):
    pass

def carregar_modelo():
    if not os.path.exists(MODELO_PATH):
        raise ModeloNaoTreinadoError(
            "Modelo não encontrado. Treine o modelo executando services/treinar_modelo.py"
        )
    return joblib.load(MODELO_PATH)

def prever_irrigacao(fosforo, potassio, ph, umidade):
    modelo = carregar_modelo()
    X = np.array([[fosforo, potassio, ph, umidade]])
    pred = modelo.predict(X)[0]
    prob = modelo.predict_proba(X).max()
    return int(pred), float(prob)
