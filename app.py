import streamlit as st
import pandas as pd
import plotly.express as px

# Título
st.title("🌤 Dashboard Clima - Cidades do Paraná")

# Carrega CSV
df = pd.read_csv("output/parana_weather.csv")

# Filtro por cidade
cidade = st.selectbox("Selecione a cidade:", df["cidade"].unique())
df_cidade = df[df["cidade"] == cidade]

st.subheader(f"Dados de {cidade}")
st.write(df_cidade)

# Gráfico de temperatura
fig_temp = px.bar(
    df,
    x="cidade",
    y="temperatura_C",
    title="Temperatura por cidade (°C)",
    labels={"temperatura_C": "Temperatura (°C)", "cidade": "Cidade"},
    color="descricao"
)
st.plotly_chart(fig_temp)

# Gráfico de sensação térmica
fig_feels = px.bar(
    df,
    x="cidade",
    y="sensacao_termica_C",
    title="Sensação térmica por cidade (°C)",
    labels={"sensacao_termica_C": "Sensação térmica (°C)", "cidade": "Cidade"},
    color="descricao"
)
st.plotly_chart(fig_feels)