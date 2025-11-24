# app_dashboard/services/fase6_service.py
from ultralytics import YOLO
import os

MODELO_YOLO_PATH = "fase6/best.pt"  # ajuste se usar outra pasta

class ModeloYOLOInexistenteError(Exception):
    pass

def carregar_modelo_yolo():
    if not os.path.exists(MODELO_YOLO_PATH):
        raise ModeloYOLOInexistenteError(
            "Modelo YOLO não encontrado. Verifique se best.pt está em fase6/best.pt"
        )
    return YOLO(MODELO_YOLO_PATH)

def analisar_imagem(caminho_imagem):
    model = carregar_modelo_yolo()
    results = model(caminho_imagem)

    # Aqui você adapta ao seu treino real:
    # Exemplo: verificar se alguma classe "praga" foi detectada
    detections = []
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            detections.append((cls_id, conf))

    return detections, results
