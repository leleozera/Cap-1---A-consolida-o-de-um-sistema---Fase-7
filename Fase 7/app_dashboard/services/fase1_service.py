# app_dashboard/services/fase1_service.py
from .db_utils import get_connection
import pandas as pd

def criar_tabela_lavoura_se_nao_existir():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS lavouras (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                area_ha REAL NOT NULL,
                cultura TEXT NOT NULL,
                insumo_principal TEXT,
                qtde_insumo_por_ha REAL
            )
        """)
        conn.commit()

def inserir_lavoura(nome, area_ha, cultura, insumo_principal, qtde_insumo_por_ha):
    criar_tabela_lavoura_se_nao_existir()
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO lavouras (nome, area_ha, cultura, insumo_principal, qtde_insumo_por_ha)
            VALUES (?, ?, ?, ?, ?)
        """, (nome, area_ha, cultura, insumo_principal, qtde_insumo_por_ha))
        conn.commit()

def listar_lavouras():
    criar_tabela_lavoura_se_nao_existir()
    with get_connection() as conn:
        df = pd.read_sql_query("SELECT * FROM lavouras", conn)
    return df
