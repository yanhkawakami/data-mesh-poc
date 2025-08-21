import pandas as pd

def get_marketing_data():
    # Simulação de dados de marketing, que poderiam vir de um banco de dados ou outro repositório
    data = {
        "campanha": ["Promoção 1", "Promoção 2", "Promoção 3"],
        "canal": ["Email", "SMS", "Push"],
        "status": ["Enviado", "Lido", "Clicado"],
        "data_envio": ["2025-04-01", "2025-04-02", "2025-04-03"]
    }
    return pd.DataFrame(data)
