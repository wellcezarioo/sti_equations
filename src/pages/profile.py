import streamlit as st
import pandas as pd
from streamlit_app import get_data, save_data, reset_data

st.markdown("# Perfil 🎉")
st.sidebar.markdown("# Perfil 🎉")

data = get_data()

# ========== Interface ==========
st.metric("Problemas Resolvidos", data["resolvidos"])
st.metric("Pontos Obtidos", data["pontos"])

st.subheader("Adicionar Progresso Manual (simulação)")

col1, col2 = st.columns(2)

with col1:
    dificuldade = st.selectbox("Dificuldade", ["Fácil", "Intermediário", "Difícil"])
    pontos = st.number_input("Pontos", min_value=1, max_value=100, value=10)
with col2:
    if st.button("Adicionar Progresso"):
        data["resolvidos"] += 1
        data["pontos"] += pontos
        data["por_dificuldade"][dificuldade] += 1
        save_data(data)
        st.success("Progresso salvo com sucesso!")
        st.rerun()

# ========== Gráfico Simples ==========
st.subheader("Distribuição por Dificuldade")

df = pd.DataFrame(
    {
        "Resolvidos": data["por_dificuldade"].values()
    },
    index=data["por_dificuldade"].keys()
)

st.bar_chart(df)

# ========== Ações ==========
st.divider()
if st.button("Resetar Progresso"):
    reset_data()
    st.success("Progresso resetado!")
    st.rerun()
