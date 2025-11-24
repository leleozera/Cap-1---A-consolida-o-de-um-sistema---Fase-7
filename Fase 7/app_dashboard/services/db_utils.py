# app_dashboard/services/db_utils.py
import sqlite3
from contextlib import contextmanager

DB_PATH = "database/sensores.db"

@contextmanager
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()
