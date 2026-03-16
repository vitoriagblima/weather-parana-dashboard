# load.py
import pandas as pd
import os

def save_weather_data(dados, output_dir="output", filename="parana_weather.csv"):
    """
    Salva todos os dados em um único arquivo CSV
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    df = pd.DataFrame(dados)
    output_path = os.path.join(output_dir, filename)
    df.to_csv(output_path, index=False)
    print(f"✔ Arquivo CSV único criado: {output_path}")

# Teste rápido
if __name__ == "__main__":
    from extract import extract_weather
    from transform import transform_weather

    raw = extract_weather()
    dados_transformados = transform_weather(raw)
    save_weather_data(dados_transformados)