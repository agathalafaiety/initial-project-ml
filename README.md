# Initial Project ML

Projeto introdutório de machine learning que utiliza regressão linear para estimar o preço de uma pizza com base em seu diâmetro.

## Tecnologias

- Python 3.11 ou superior
- Pandas
- Scikit-learn
- Streamlit
- Poetry

## Estrutura

```text
initial-project-ml/
├── app/          # Interface com Streamlit
├── data/         # Dados usados no treinamento
├── notebooks/    # Análise e experimentos
├── src/          # Código do modelo
└── tests/        # Testes automatizados
```

## Como executar

Instale as dependências:

```bash
poetry install
```

Inicie a aplicação:

```bash
poetry run streamlit run app/app.py
```

Depois, acesse o endereço exibido no terminal e informe o diâmetro da pizza para obter uma estimativa de preço.

Desenvolvido por [Agatha Lafaiety](https://github.com/agathalafaiety).
