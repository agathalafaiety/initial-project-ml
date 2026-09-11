import streamlit as st

from projeto_ml.modelo import prever_preco, treinar_modelo


modelo = treinar_modelo()

st.title("Previsão do preço de uma pizza")
st.divider()

diametro = st.number_input(
    "Digite o diâmetro da pizza (cm)",
    min_value=0.0,
    step=1.0,
)

if diametro > 0:
    preco_previsto = prever_preco(modelo, diametro)
    st.write(
        f"O valor estimado para uma pizza de {diametro:.2f} cm "
        f"é R$ {preco_previsto:.2f}."
    )
