FIAP - Faculdade de Informática e Administração Paulista

FIAP - Faculdade de Informática e Admnistração Paulista


Cap 1 - A consolidação de um sistema

Nome do grupo

👨‍🎓 Integrantes:
Erick Souza Pereira
Leonardo Nunes Urbano

👩‍🏫 Professores:

Tutor(a)

Nome do Tutor

Coordenador(a)

Nome do Coordenador

📜 Descrição

Este projeto faz parte da Fase 7 do Programa de Formação da FIAP e representa a consolidação de todas as etapas desenvolvidas nas Fases 1 a 6. O objetivo final é integrar em um único sistema todos os serviços criados anteriormente, criando um ecossistema digital completo para gestão agrícola, que pode ser facilmente adaptado para outros setores da economia.

Ao longo do desenvolvimento, foram trabalhados tópicos essenciais como IoT, Banco de Dados, Automação, Machine Learning, Cloud Computing, Segurança da Informação e Visão Computacional. Na Fase 7, esses elementos são organizados em um único dashboard interativo desenvolvido em Python com Streamlit.
- **Fase 1 – Base de Dados Inicial:** Cálculo de áreas de plantio, manejo de insumos e integração com API meteorológica, com análises estatísticas em R.
- **Fase 2 – Banco de Dados Relacional:** Criação de MER/DER e estrutura de tabelas para armazenar insumos, lavouras, sensores e leituras.
- **Fase 3 – IoT e Automação:** Simulação de sensores com ESP32 integrados ao banco SQL, possibilitando CRUD em tempo real e controle automático de irrigação.
- **Fase 4 – Machine Learning e Dashboard:** Criação de um modelo Random Forest e integração via Streamlit em um dashboard interativo.
- **Fase 5 – Cloud e Segurança:** Hospedagem e configuração AWS com boas práticas baseadas em ISO 27001 e 27002.
- **Fase 6 – Visão Computacional:** Implementação de modelo YOLO para detectar anomalias, pragas e doenças por imagens.
- **Fase 7 – Consolidação:** Integração total das fases anteriores em uma plataforma única, com disparo automático de alertas utilizando AWS SNS.

### **Principais Funcionalidades da Fase 7**
- Dashboard com abas integradas para Fase 1, 3, 4 e 6.  
- Previsão de irrigação usando Machine Learning.  
- Detecção de pragas usando IA e YOLO.  
- Banco de dados único para leituras, lavouras e sensores.  
- Disparo automático de alertas via SMS/E-mail usando AWS SNS.  
- Estrutura de projeto profissional, escalável e reutilizável.

📁 Estrutura de pastas
Cap-1---A-consolida-o-de-um-sistema---Fase-7-main/
│
└── Fase 7/
    │
    ├── Fase 1/
    │   └── programa1.py
    │
    ├── Fase 2/
    │   ├── Script_DDL_Projetofase2cap1_SIP.sql
    │   └── TRABALHO_CAP6_FASE2.py
    │
    ├── Fase 3/
    │   ├── criar_branco.py
    │   ├── sensores.db
    │   ├── branco/
    │   │   └── criar_tabelas.sql
    │   └── dados/
    │       └── sensores.db
    │
    ├── Fase 4/
    │   ├── database/
    │   ├── modelo/
    │   └── python/
    │
    ├── Fase 6/
    │   ├── YOLOv8/
    │   ├── imagens/
    │   ├── resultados/
    │   └── yolo_service.py
    │
    ├── app_dashboard/
    │   ├── .env
    │   ├── .venv/
    │   ├── app.py
    │   ├── requirements.txt
    │   │
    │   ├── database/
    │   │   ├── sensores.db
    │   │   └── leituras_sensor/
    │   │
    │   ├── models/
    │   │   └── modelo_rf.pkl
    │   │
    │   └── services/
    │       ├── aws_alertas_service.py
    │       ├── db_utils.py
    │       ├── fase1_service.py
    │       ├── fase3_service.py
    │       ├── fase6_service.py
    │       ├── ml_service.py
    │       └── treinar_modelo.py
    │
    └── testar_sn.py


🔧 Como executar o código
### **📌 Requisitos**
- Python 3.13+  
- Pip atualizado  
- Streamlit  
- Boto3  
- Biblioteca python-dotenv  
- YOLO (Ultralytics)  
- Banco SQLite  
- Conta AWS configurada com SNS e credenciais IAM

📹 Link do vídeo: https://youtu.be/tWi5ntBsuec


🗃 Histórico de lançamentos
0.5.0 - 23/11/2025 *
0.4.0 - XX/XX/2025 *
0.3.0 - XX/XX/2025 *
0.2.0 - XX/XX/2025 *
0.1.0 - XX/XX/2025 *
📋 Licença


MODELO GIT FIAP por Fiap está licenciado sobre Attribution 4.0 International.
