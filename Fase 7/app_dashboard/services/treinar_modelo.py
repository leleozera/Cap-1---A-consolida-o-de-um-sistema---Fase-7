# app_dashboard/services/treinar_modelo.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from .db_utils import get_connection
import joblib
import os

MODELO_PATH = "models/modelo_rf.pkl"

def treinar_modelo():
    # Carregar dados do banco
    with get_connection() as conn:
        df = pd.read_sql_query("SELECT * FROM leituras", conn)

    X = df[['fosforo', 'potassio', 'ph', 'umidade']]
    y = df['irrigacao_ativa']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Salvar modelo treinado
    os.makedirs("models", exist_ok=True)
    joblib.dump(clf, MODELO_PATH)
    print(f"Modelo salvo em {MODELO_PATH}")

if __name__ == "__main__":
    treinar_modelo()
