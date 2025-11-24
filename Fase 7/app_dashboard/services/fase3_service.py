# app_dashboard/services/fase3_service.py
import pandas as pd
from .db_utils import get_connection

def listar_leituras():
    with get_connection() as conn:
        df = pd.read_sql_query("SELECT * FROM leituras ORDER BY timestamp DESC", conn)
    return df

def inserir_leitura(fosforo, potassio, ph, umidade, irrigacao_ativa):
    from datetime import datetime
    timestamp = datetime.now().isoformat(timespec="seconds")
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO leituras (timestamp, fosforo, potassio, ph, umidade, irrigacao_ativa)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (timestamp, fosforo, potassio, ph, umidade, int(irrigacao_ativa)),
        )
        conn.commit()
