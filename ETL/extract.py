# extract.py
import os
import requests
from dotenv import load_dotenv
import time

load_dotenv()
api_key = os.getenv("RAPIDAPI_KEY")

url = "https://open-weather13.p.rapidapi.com/city"
headers = {
    "x-rapidapi-key": api_key,
    "x-rapidapi-host": "open-weather13.p.rapidapi.com",
    "Content-Type": "application/json"
}

cidades_parana = [
    "Curitiba", "Londrina", "Maringá", "Ponta Grossa", "Cascavel",
    "Foz do Iguaçu", "São José dos Pinhais", "Colombo", "Guarapuava"
]

def extract_weather():
    resultados = []
    for cidade in cidades_parana:
        querystring = {"city": cidade, "lang": "PT"}
        try:
            response = requests.get(url, headers=headers, params=querystring, timeout=10)
            response.raise_for_status()
            resultados.append(response.json())
            print(f"✔ Dados extraídos: {cidade}")
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao buscar {cidade}: {e}")
        time.sleep(1)  # evita sobrecarga da API
    return resultados

if __name__ == "__main__":
    dados = extract_weather()
    print(f"Extração concluída: {len(dados)} cidades")