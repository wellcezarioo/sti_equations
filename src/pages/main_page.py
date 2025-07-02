import streamlit as st

import solver

from pages.problems import set_random_problem

change_type_tips = {
    # Transformações diretamente usadas para isolar x
    "ADD_TO_BOTH_SIDES": "Adicione o mesmo valor aos dois lados da equação.",
    "SUBTRACT_FROM_BOTH_SIDES": "Subtraia o mesmo valor dos dois lados da equação.",
    "MULTIPLY_TO_BOTH_SIDES": "Multiplique os dois lados da equação pelo mesmo valor.",
    "DIVIDE_FROM_BOTH_SIDES": "Divida os dois lados da equação pelo mesmo valor.",
    "MULTIPLY_BOTH_SIDES_BY_INVERSE_FRACTION": "Multiplique ambos os lados pelo inverso da fração.",
    "MULTIPLY_BOTH_SIDES_BY_NEGATIVE_ONE": "Multiplique os dois lados por -1 para trocar o sinal.",
    "SWAP_SIDES": "Troque os lados da equação para facilitar a leitura.",

    # Simplificações algébricas comuns
    "SIMPLIFY_ARITHMETIC": "Resolva contas simples (como somas ou multiplicações).",
    "SIMPLIFY_LEFT_SIDE": "Simplifique a expressão do lado esquerdo.",
    "SIMPLIFY_RIGHT_SIDE": "Simplifique a expressão do lado direito.",
    "COLLECT_AND_COMBINE_LIKE_TERMS": "Agrupe e some os termos semelhantes.",
    "COLLECT_LIKE_TERMS": "Agrupe os termos semelhantes.",
    "REARRANGE_COEFF": "Reorganize os coeficientes para facilitar a leitura.",
    "ADD_POLYNOMIAL_TERMS": "Some os termos do polinômio que são semelhantes.",
    "ADD_COEFFICIENT_OF_ONE": "Adicione o coeficiente 1 onde ele está implícito.",
    "UNARY_MINUS_TO_NEGATIVE_ONE": "Converta o sinal de menos para -1 vezes o termo.",
    "REMOVE_ADDING_ZERO": "Remova a adição de zero, pois não altera o valor.",
    "REMOVE_MULTIPLYING_BY_ONE": "Remova a multiplicação por 1, pois não altera o valor.",
    "REMOVE_MULTIPLYING_BY_NEGATIVE_ONE": "Remova a multiplicação por -1 ao simplificar o sinal.",
    "RESOLVE_DOUBLE_MINUS": "Dois sinais de menos se anulam: transforme em mais.",

    # Simplificações envolvendo frações
    "SIMPLIFY_FRACTION": "Simplifique a fração dividindo numerador e denominador por um fator comum.",
    "SIMPLIFY_SIGNS": "Ajuste os sinais da fração (ex: -a/-b = a/b).",
    "CANCEL_TERMS": "Cancele termos iguais no numerador e denominador.",
    "CANCEL_MINUSES": "Elimine sinais de menos duplicados.",
    "MULTIPLY_BY_INVERSE": "Multiplique por uma fração invertida para facilitar a resolução.",

    # Verificação de conclusão
    "STATEMENT_IS_TRUE": "A equação foi resolvida corretamente (verdadeiro).",
    "STATEMENT_IS_FALSE": "A equação não tem solução (falsa)."
}

# Main page content
st.markdown("# Math Tutor: First-Degree Equations")
st.sidebar.markdown("# Main page 🎈")

# Inicializa estados
if "current_problem" not in st.session_state:
    st.session_state.current_problem = "2*x + 3 = 7"
if "solve_for" not in st.session_state:
    st.session_state.solve_for = "x"
if "user_answer" not in st.session_state:
    st.session_state.user_answer = ""
if "hint_pos" not in st.session_state:
    st.session_state.hint_pos = 0
if "solution_steps" not in st.session_state:
    st.session_state.solution_steps = [
        {"changeType": "ADD_TO_BOTH_SIDES", "changeGroup": "ADD_TO_BOTH_SIDES", "substeps": []},
        {"changeType": "SIMPLIFY_ARITHMETIC", "changeGroup": "SIMPLIFY_ARITHMETIC", "substeps": []},
        {"changeType": "DIVIDE_FROM_BOTH_SIDES", "changeGroup": "DIVIDE_FROM_BOTH_SIDES", "substeps": []},
        {"changeType": "SIMPLIFY_ARITHMETIC", "changeGroup": "SIMPLIFY_ARITHMETIC", "substeps": []}
    ]

<<<<<<< Updated upstream
=======
# Função para gerar novo problema (simulação)
def gerar_novo_problema():
    # Aqui você pode integrar com um gerador real depois
    st.session_state.current_problem = "3x - 4 = 5"
    st.session_state.solve_for = "x"
    st.session_state.user_answer = ""
    st.session_state.solution_steps = [
        {"changeType": "ADD_TO_BOTH_SIDES", "changeGroup": "ADD_TO_BOTH_SIDES", "substeps": []},
        {"changeType": "SIMPLIFY_ARITHMETIC", "changeGroup": "SIMPLIFY_ARITHMETIC", "substeps": []},
        {"changeType": "DIVIDE_FROM_BOTH_SIDES", "changeGroup": "DIVIDE_FROM_BOTH_SIDES", "substeps": []},
        {"changeType": "SIMPLIFY_ARITHMETIC", "changeGroup": "SIMPLIFY_ARITHMETIC", "substeps": []}
    ]
    st.session_state.hint_pos = 0

>>>>>>> Stashed changes
# Função para exibir uma dica (simulação)
def mostrar_dica():
    num_dicas = len(st.session_state.solution_steps)
    if num_dicas == 0:
        st.warning("Não há dicas para este problema.")
        return

    # Mostra a dica atual
    st.info(change_type_tips[st.session_state.solution_steps[st.session_state.hint_pos]["changeType"]])

    # Avança para a próxima dica, voltando ao início se chegar ao fim
    st.session_state.hint_pos = (st.session_state.hint_pos + 1) % num_dicas

@st.dialog("Solução")
def display_result(result):
    if result:
        st.success("Parabéns. Solução correta. Tente um novo problema.")
        set_random_problem()
    else:
        st.error("Solução incorreta. Tente novamente, ou utilize dicas.")

with st.container(border=True):
    # Título com emoji
    st.markdown("### 🧠 Problema Atual")

    # Exibição do problema
    st.markdown(f"**Equação:**")
    st.markdown(f"#### {st.session_state.current_problem}")
    st.caption(f"**Resolva para:** `{st.session_state.solve_for}`")

    with st.form('problem'):
<<<<<<< Updated upstream
        st.session_state.user_answer = st.text_input("Sua resposta:", st.session_state.user_answer)
        submit = st.form_submit_button('Enviar solução')
=======
        st.text_input("Sua resposta:", key="user_answer")
        submit = st.form_submit_button('Submit')
>>>>>>> Stashed changes

    if submit:
        user_input = st.session_state.user_answer.strip()
        if not user_input:
            st.error("Por favor, insira sua resposta.")
        else:
            try:
                # Substitui vírgula por ponto para garantir a conversão correta para float
                user_answer_float = float(user_input.replace(',', '.'))
                is_correct = abs(solver.get_equation_solution(st.session_state.current_problem, st.session_state.solve_for) - user_answer_float) <= 0.0001
                display_result(is_correct)
            except ValueError:
                st.error("Por favor, insira uma resposta numérica válida.")
            except TypeError:
                st.error("Ocorreu um erro inesperado com a sua resposta. Tente novamente.")

    # Botões adicionais
    col1, col2 = st.columns(2)

    with col1:
        if st.button("💡 Obter uma dica"):
            mostrar_dica()

    with col2:
<<<<<<< Updated upstream
        if st.button("🔄 Novo problema"):
            set_random_problem()
=======
        if st.button("🔄 Novo problema", on_click=gerar_novo_problema):
            pass
>>>>>>> Stashed changes

