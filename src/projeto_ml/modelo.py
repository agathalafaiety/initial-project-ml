from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression


CAMINHO_DADOS = Path(__file__).resolve().parents[2] / "data" / "pizzas.csv"


def carregar_dados(caminho: Path = CAMINHO_DADOS) -> pd.DataFrame:
    """Carrega os dados usados para treinar o modelo."""
    return pd.read_csv(caminho)


def treinar_modelo(dados: pd.DataFrame | None = None) -> LinearRegression:
    """Treina uma regressão linear com diâmetro e preço das pizzas."""
    if dados is None:
        dados = carregar_dados()

    modelo = LinearRegression()
    modelo.fit(dados[["diametro"]], dados["preco"])
    return modelo


def prever_preco(modelo: LinearRegression, diametro: float) -> float:
    """Retorna o preço estimado para o diâmetro informado."""
    entrada = pd.DataFrame({"diametro": [diametro]})
    return float(modelo.predict(entrada)[0])
