# app.py
import streamlit as st
import pandas as pd
import requests
import os
from dotenv import load_dotenv
import time
import plotly.express as px

# Carrega variáveis do .env
load_dotenv()
api_key = os.getenv("RAPIDAPI_KEY")

st.set_page_config(page_title="🌤 Dashboard Clima - Paraná", layout="wide")
st.title("🌤 Dashboard Clima - Cidades do Paraná")

# Lista de cidades
cidades_parana = [
    "Curitiba", "Londrina", "Maringá", "Ponta Grossa", "Cascavel",
    "Foz do Iguaçu", "São José dos Pinhais", "Colombo", "Guarapuava"
]

# Configura API
url = "https://open-weather13.p.rapidapi.com/city"
headers = {
    "x-rapidapi-key": api_key,
    "x-rapidapi-host": "open-weather13.p.rapidapi.com",
    "Content-Type": "application/json"
}

# Extrai dados da API
dados = []
with st.spinner("Buscando dados da API..."):
    for cidade in cidades_parana:
        querystring = {"city": cidade, "lang": "PT"}
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            r = response.json()
            temp_c = (r["main"].get("temp") - 32) * 5/9
            feels_like_c = (r["main"].get("feels_like") - 32) * 5/9
            dados.append({
                "cidade": r.get("name"),
                "temperatura_C": round(temp_c, 2),
                "sensacao_termica_C": round(feels_like_c, 2),
                "umidade": r["main"].get("humidity"),
                "pressao": r["main"].get("pressure"),
                "descricao": r["weather"][0].get("description"),
                "vento_velocidade": r["wind"].get("speed"),
                "vento_direcao": r["wind"].get("deg")
            })
        else:
            st.warning(f"Erro ao buscar {cidade}: {response.status_code}")
        time.sleep(1)

df = pd.DataFrame(dados)

# Filtro por cidade
cidade_selecionada = st.selectbox("Selecione a cidade:", df["cidade"].unique())
df_cidade = df[df["cidade"] == cidade_selecionada]

st.subheader(f"Dados de {cidade_selecionada}")
st.dataframe(df_cidade)

# Gráfico de temperatura por cidade
fig_temp = px.bar(
    df,
    x="cidade",
    y="temperatura_C",
    color="descricao",
    labels={"temperatura_C": "Temperatura (°C)", "cidade": "Cidade"},
    title="🌡 Temperatura por cidade"
)
st.plotly_chart(fig_temp, use_container_width=True)

# Gráfico de sensação térmica por cidade
fig_feels = px.bar(
    df,
    x="cidade",
    y="sensacao_termica_C",
    color="descricao",
    labels={"sensacao_termica_C": "Sensação térmica (°C)", "cidade": "Cidade"},
    title="🤒 Sensação térmica por cidade"
)
st.plotly_chart(fig_feels, use_container_width=True)

# Gráfico de umidade
fig_humidity = px.bar(
    df,
    x="cidade",
    y="umidade",
    labels={"umidade": "Umidade (%)", "cidade": "Cidade"},
    title="💧 Umidade por cidade"
)
st.plotly_chart(fig_humidity, use_container_width=True)