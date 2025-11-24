import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Conectar e carregar dados
conn = sqlite3.connect('../database/sensores.db')
df = pd.read_sql_query("SELECT * FROM leituras", conn)
conn.close()

# Features (entradas) e target (saída)
X = df[['fosforo', 'potassio', 'ph', 'umidade']]
y = df['irrigacao_ativa']

# Dividir dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinar modelo de classificação
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Avaliação do modelo
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
