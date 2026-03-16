# transform.py
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def transform_weather(raw_data):
    dados_transformados = []
    for resultado in raw_data:
        temp_c = fahrenheit_to_celsius(resultado["main"].get("temp"))
        feels_like_c = fahrenheit_to_celsius(resultado["main"].get("feels_like"))
        dados_transformados.append({
            "cidade": resultado.get("name"),
            "temperatura_C": round(temp_c, 2),
            "sensacao_termica_C": round(feels_like_c, 2),
            "umidade": resultado["main"].get("humidity"),
            "pressao": resultado["main"].get("pressure"),
            "descricao": resultado["weather"][0].get("description"),
            "vento_velocidade": resultado["wind"].get("speed"),
            "vento_direcao": resultado["wind"].get("deg")
        })
    return dados_transformados

if __name__ == "__main__":
    from extract import extract_weather
    raw = extract_weather()
    dados = transform_weather(raw)
    print(f"Transformação concluída: {len(dados)} registros")