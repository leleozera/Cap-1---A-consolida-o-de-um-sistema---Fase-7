import streamlit as st
import pandas as pd

from services.fase1_service import (
    inserir_lavoura,
    listar_lavouras,
    criar_tabela_lavoura_se_nao_existir,
)
from services.fase3_service import listar_leituras, inserir_leitura
from services.ml_service import prever_irrigacao, ModeloNaoTreinadoError
from services.fase6_service import analisar_imagem, ModeloYOLOInexistenteError
from services.aws_alertas_service import enviar_alerta

st.set_page_config(page_title="FarmTech - Sistema Integrado", layout="wide")

st.sidebar.title("Navegação")
pagina = st.sidebar.selectbox(
    "Selecione a seção",
    [
        "Visão Geral",
        "Fase 1 - Lavoura",
        "Fase 3 - Sensores & Irrigação",
        "Fase 4 - ML (Previsão)",
        "Fase 6 - Visão Computacional",
        "Alertas & AWS",
    ],
)

st.title("Dashboard Integrada - FarmTech Solutions")

# === VISÃO GERAL ===
if pagina == "Visão Geral":
    st.subheader("Resumo dos Sensores (Fase 3 / 4)")

    try:
        df = listar_leituras()
        if df.empty:
            st.info("Nenhuma leitura registrada ainda.")
        else:
            col1, col2 = st.columns(2)

            with col1:
                st.write("Leituras recentes")
                st.dataframe(df.head(10))

            with col2:
                st.write("Gráfico de Umidade")
                st.line_chart(df.set_index("timestamp")["umidade"])

                st.write("Gráfico de pH")
                st.line_chart(df.set_index("timestamp")["ph"])

            st.write("Resumo estatístico")
            st.write(df[["fosforo", "potassio", "ph", "umidade"]].describe())
    except Exception as e:
        st.error(f"Erro ao carregar leituras: {e}")


# === FASE 1 - LAVOURA ===
elif pagina == "Fase 1 - Lavoura":
    st.subheader("Cadastro e Visualização da Lavoura")

    criar_tabela_lavoura_se_nao_existir()

    with st.form("form_lavoura"):
        nome = st.text_input("Nome da área (ex: Talhão 1)")
        area_ha = st.number_input("Área (ha)", min_value=0.0, step=0.1)
        cultura = st.text_input("Cultura (ex: Soja, Milho)")
        insumo_principal = st.text_input("Insumo principal (ex: NPK 20-05-20)")
        qtde_insumo_por_ha = st.number_input("Qtd. de insumo por ha (kg/ha)", min_value=0.0, step=0.1)

        submitted = st.form_submit_button("Cadastrar lavoura")

    if submitted:
        inserir_lavoura(nome, area_ha, cultura, insumo_principal, qtde_insumo_por_ha)
        st.success("Lavoura cadastrada com sucesso!")

    st.markdown("---")
    st.write("Lavouras cadastradas:")

    df_lav = listar_lavouras()
    if df_lav.empty:
        st.info("Nenhuma lavoura cadastrada ainda.")
    else:
        st.dataframe(df_lav)


# === FASE 3 - SENSORES & IRRIGAÇÃO ===
elif pagina == "Fase 3 - Sensores & Irrigação":
    st.subheader("Leituras dos sensores e inserção manual")

    df = listar_leituras()
    if df.empty:
        st.info("Nenhuma leitura registrada ainda.")
    else:
        st.dataframe(df)

    st.markdown("### Inserir leitura simulada")

    with st.form("form_leitura"):
        fosforo = st.number_input("Fósforo (ppm)", min_value=0, max_value=500, step=1)
        potassio = st.number_input("Potássio (ppm)", min_value=0, max_value=500, step=1)
        ph = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1)
        umidade = st.number_input("Umidade (%)", min_value=0.0, max_value=100.0, step=0.1)
        irrigacao_ativa = st.checkbox("Irrigação estava ativa?")

        enviar = st.form_submit_button("Salvar leitura")

    if enviar:
        inserir_leitura(fosforo, potassio, ph, umidade, irrigacao_ativa)
        st.success("Leitura inserida com sucesso! Atualize a página para ver na tabela.")


# === FASE 4 - ML (PREVISÃO) ===
elif pagina == "Fase 4 - ML (Previsão)":
    st.subheader("Previsão de necessidade de irrigação (Random Forest)")

    with st.form("form_ml"):
        fosforo = st.number_input("Fósforo (ppm)", min_value=0, max_value=500, step=1)
        potassio = st.number_input("Potássio (ppm)", min_value=0, max_value=500, step=1)
        ph = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1)
        umidade = st.number_input("Umidade (%)", min_value=0.0, max_value=100.0, step=0.1)

        prever = st.form_submit_button("Prever irrigação")

    if prever:
        try:
            pred, prob = prever_irrigacao(fosforo, potassio, ph, umidade)

            if pred == 1:
                st.error(f"Previsão: ATIVAR irrigação (confiança ~ {prob:.2f})")

                # 🚨 DISPARA ALERTA NA AWS
                mensagem = (
                    "Alerta de irrigação automática:\n"
                    f"- Fósforo: {fosforo} ppm\n"
                    f"- Potássio: {potassio} ppm\n"
                    f"- pH: {ph}\n"
                    f"- Umidade: {umidade}%\n\n"
                    "A recomendação do modelo é ATIVAR a irrigação. "
                    "Verificar bombas e válvulas da área monitorada."
                )
                try:
                    enviar_alerta(mensagem, "Alerta de Irrigação - FarmTech")
                    st.success("Alerta enviado para a equipe da fazenda (AWS SNS).")
                except Exception as e:
                    st.warning(f"Não foi possível enviar o alerta AWS: {e}")

            else:
                st.success(f"Previsão: NÃO é necessário ativar irrigação agora (confiança ~ {prob:.2f})")

        except ModeloNaoTreinadoError as e:
            st.warning(str(e))
        except Exception as e:
            st.error(f"Erro ao prever: {e}")



# === FASE 6 - VISÃO COMPUTACIONAL ===
elif pagina == "Fase 6 - Visão Computacional":
    st.subheader("Análise de imagem da lavoura (YOLO)")

    uploaded_file = st.file_uploader("Envie uma imagem da plantação", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        import tempfile
        from PIL import Image

        img = Image.open(uploaded_file)
        tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        img.save(tmp_file.name)

        st.image(img, caption="Imagem enviada", use_column_width=True)

        try:
            detections, results = analisar_imagem(tmp_file.name)
            st.write("Detecções brutas:", detections)

            if len(detections) > 0:
                st.error("Possível anomalia detectada (ex.: praga/doença).")

                # 🚨 ALERTA DE PRAGA DO YOLO
                mensagem = (
                    "Alerta de pragas na lavoura:\n"
                    "O sistema de visão computacional (YOLO) detectou anomalias na imagem enviada.\n"
                    "Recomenda-se inspeção imediata da área e aplicação de defensivos, se necessário."
                )
                try:
                    enviar_alerta(mensagem, "Alerta de Pragas - FarmTech")
                    st.success("Alerta enviado para a equipe da fazenda (AWS SNS).")
                except Exception as e:
                    st.warning(f"Não foi possível enviar o alerta AWS: {e}")
            else:
                st.success("Nenhuma anomalia relevante detectada.")

        except ModeloYOLOInexistenteError as e:
            st.warning(str(e))
        except Exception as e:
            st.error(f"Erro ao analisar imagem: {e}")



# === ALERTAS & AWS ===
elif pagina == "Alertas & AWS":
    st.subheader("Disparo manual de alertas (AWS SNS)")

    st.markdown("""
    Use esta área para enviar alertas manuais para o time da fazenda via AWS SNS.
    Em produção, esses alertas seriam disparados automaticamente a partir de regras de negócio.
    """)

    mensagem = st.text_area(
        "Mensagem do alerta",
        "Alerta manual: verificar sistema de irrigação da área 1."
    )

    assunto = st.text_input("Assunto do alerta", "Alerta Manual - FarmTech")

    if st.button("Enviar alerta agora"):
        try:
            enviar_alerta(mensagem, assunto)
            st.success("Alerta enviado com sucesso via AWS SNS! Verifique seu email/SMS.")
        except Exception as e:
            st.error(f"Erro ao enviar alerta: {e}")
