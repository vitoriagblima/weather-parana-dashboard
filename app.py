import streamlit as st
import pandas as pd
import subprocess
import os

st.set_page_config(page_title="🌤 Dashboard Clima - Paraná", layout="wide")
st.title("🌤 Dashboard Clima - Cidades do Paraná")

csv_path = "output/parana_weather.csv"

# --- Executa o pipeline ETL ---
st.info("Rodando pipeline ETL para atualizar os dados...")

try:
    # Chama o script run_pipeline.py do seu ETL
    subprocess.run(["python", "etl/run_pipeline.py"], check=True)
except subprocess.CalledProcessError as e:
    st.error("Erro ao executar o ETL. Verifique os logs do ETL.")
    st.stop()

# --- Verifica se o CSV foi gerado ---
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)

    if df.empty:
        st.error("O CSV gerado pelo ETL está vazio. Possível erro na API.")
    else:
        # Filtro por cidade
        cidade_selecionada = st.selectbox("Selecione a cidade:", df["cidade"].unique())
        df_cidade = df[df["cidade"] == cidade_selecionada]

        st.subheader(f"Dados de {cidade_selecionada}")
        st.dataframe(df_cidade)

        # Gráficos
        import plotly.express as px

        fig_temp = px.bar(
            df, x="cidade", y="temperatura_C", color="descricao",
            labels={"temperatura_C": "Temperatura (°C)", "cidade": "Cidade"},
            title="🌡 Temperatura por cidade"
        )
        st.plotly_chart(fig_temp, use_container_width=True)

        fig_feels = px.bar(
            df, x="cidade", y="sensacao_termica_C", color="descricao",
            labels={"sensacao_termica_C": "Sensação térmica (°C)", "cidade": "Cidade"},
            title="🤒 Sensação térmica por cidade"
        )
        st.plotly_chart(fig_feels, use_container_width=True)

        fig_humidity = px.bar(
            df, x="cidade", y="umidade",
            labels={"umidade": "Umidade (%)", "cidade": "Cidade"},
            title="💧 Umidade por cidade"
        )
        st.plotly_chart(fig_humidity, use_container_width=True)
else:
    st.error("Arquivo CSV não encontrado após execução do ETL. Verifique os logs do ETL.")