# services/aws_alertas_service.py

import os
import boto3
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
TOPIC_ARN = os.getenv("AWS_SNS_TOPIC_ARN")


def get_sns_client():
    """
    Cria um client SNS usando EXATAMENTE as credenciais do .env.
    """
    if not AWS_ACCESS_KEY or not AWS_SECRET_KEY:
        raise RuntimeError("Chaves AWS não encontradas no .env")

    if not AWS_REGION:
        raise RuntimeError("AWS_REGION não definida no .env")

    return boto3.client(
        "sns",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION,
    )


def enviar_alerta(mensagem: str, assunto: str = "Alerta FarmTech"):
    """
    Envia um alerta via SNS para o tópico configurado no .env.
    """
    if not TOPIC_ARN:
        raise RuntimeError("AWS_SNS_TOPIC_ARN não definido no .env")

    sns = get_sns_client()

    resp = sns.publish(
        TopicArn=TOPIC_ARN,
        Message=mensagem,
        Subject=assunto,
    )

    print("Mensagem publicada. MessageId:", resp.get("MessageId"))
