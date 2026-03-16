# run_pipeline.py
import sys
import os

etl_path = os.path.join(os.path.dirname(__file__), "etl")
sys.path.append(etl_path)

from extract import extract_weather
from transform import transform_weather
from load import save_weather_data

def run_pipeline():
    print("🔹 Iniciando pipeline ETL...")
    
    # Extração
    print("1 - Extração de dados da API...")
    raw_data = extract_weather()
    print(f"✔ Extração concluída: {len(raw_data)} cidades")

    # Transformação
    print("2 - Transformação dos dados...")
    transformed_data = transform_weather(raw_data)
    print(f"✔ Transformação concluída: {len(transformed_data)} registros")

    # Carga
    print("3 - Salvando os dados em arquivos CSV...")
    save_weather_data(transformed_data)
    print("✔ Pipeline concluído com sucesso!")

if __name__ == "__main__":
    run_pipeline()