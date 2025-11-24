import sqlite3
from datetime import datetime

# Criar conexão SQLite (arquivo banco.db)
conn = sqlite3.connect('sensores.db')
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS leituras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    fosforo INTEGER NOT NULL,
    potassio INTEGER NOT NULL,
    ph REAL NOT NULL,
    umidade REAL NOT NULL,
    irrigacao_ativa INTEGER NOT NULL
)
''')
conn.commit()

# Função inserir dado
def inserir_leitura(fosforo, potassio, ph, umidade, irrigacao):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
    INSERT INTO leituras (timestamp, fosforo, potassio, ph, umidade, irrigacao_ativa)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (ts, fosforo, potassio, ph, umidade, irrigacao))
    conn.commit()
    print(f"Leitura inserida em {ts}")

# Função consultar dados
def consultar_todas():
    cursor.execute('SELECT * FROM leituras')
    for row in cursor.fetchall():
        print(row)

# Função atualizar dado (exemplo: atualizar umidade da leitura id=1)
def atualizar_umidade(id_leitura, nova_umidade):
    cursor.execute('UPDATE leituras SET umidade = ? WHERE id = ?', (nova_umidade, id_leitura))
    conn.commit()
    print(f"Umidade da leitura {id_leitura} atualizada para {nova_umidade}")

# Função apagar dado (exemplo: apagar leitura id=1)
def apagar_leitura(id_leitura):
    cursor.execute('DELETE FROM leituras WHERE id = ?', (id_leitura,))
    conn.commit()
    print(f"Leitura {id_leitura} apagada")

# Simulação de inserção de dados (como se viessem do ESP32)
inserir_leitura(fosforo=1, potassio=0, ph=6.7, umidade=35.4, irrigacao=1)
inserir_leitura(fosforo=1, potassio=1, ph=7.0, umidade=45.0, irrigacao=0)

print("\nConsultando todas as leituras:")
consultar_todas()

# Atualiza umidade na primeira leitura
atualizar_umidade(1, 40.0)

# Apaga a segunda leitura
apagar_leitura(2)

print("\nConsultando todas as leituras após atualização e exclusão:")
consultar_todas()

# Fechar conexão no final
conn.close()
