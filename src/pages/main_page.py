import streamlit as st

from solver import get_equation_solution

# Main page content
st.markdown("# Math Tutor: First-Degree Equations")
st.sidebar.markdown("# Main page 🎈")

import streamlit as st

# Inicializa estados
if "current_problem" not in st.session_state:
    st.session_state.current_problem = "2*x + 3 = 7"
if "solve_for" not in st.session_state:
    st.session_state.solve_for = "x"
if "user_answer" not in st.session_state:
    st.session_state.user_answer = ""

# Função para gerar novo problema (simulação)
def gerar_novo_problema():
    # Aqui você pode integrar com um gerador real depois
    st.session_state.current_problem = "3x - 4 = 5"
    st.session_state.solve_for = "x"
    st.session_state.user_answer = ""

# Função para exibir uma dica (simulação)
def mostrar_dica():
    st.info("Tente isolar o x em um dos lados da equação.")


@st.dialog("Cast your vote")
def display_result(result):
    st.write(f'{"Correct" if result else "Incorrect"} solution!')

with st.container(border=True):
    # Título com emoji
    st.markdown("### 🧠 Current Problem")

    # Exibição do problema
    st.markdown(f"**Equação:** {st.session_state.current_problem}")
    st.caption(f"**Resolva para:** `{st.session_state.solve_for}`")

    with st.form('problem'):
        st.session_state.user_answer = st.text_input("Sua resposta:", st.session_state.user_answer)
        submit = st.form_submit_button('Submit')

    if submit:
        display_result((get_equation_solution(st.session_state.current_problem, st.session_state.solve_for) - float(st.session_state.user_answer) <= 0.0001))

    # Botões adicionais
    col1, col2 = st.columns(2)

    with col1:
        if st.button("💡 Obter uma dica"):
            mostrar_dica()

    with col2:
        if st.button("🔄 Novo problema"):
            gerar_novo_problema()
