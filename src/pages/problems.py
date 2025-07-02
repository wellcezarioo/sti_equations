import streamlit as st
import solver
import random

st.sidebar.markdown("# Problemas ❄️")

equation_sets = {
    "Fácil": [
        {"equation": "x - 6 = 12", "variable": "x"},
        {"equation": "y + 1 = 33", "variable": "y"},
        {"equation": "10 + z = 53", "variable": "z"},
        {"equation": "a - 90 = 180", "variable": "a"},
        {"equation": "8 + x = -25", "variable": "x"},
        {"equation": "-30 + y = 7", "variable": "y"},
        {"equation": "180 + b = 181", "variable": "b"},
        {"equation": "-200 + x = 200", "variable": "x"},
        {"equation": "-z + 3 = 0", "variable": "z"},
        {"equation": "41 - y = 22", "variable": "y"},
    ],
    "Médio": [
        {"equation": "3*a + 2 = 4", "variable": "a"},
        {"equation": "2*z + 1 = 0", "variable": "z"},
        {"equation": "-12 + 4*y = 0", "variable": "y"},
        {"equation": "-5*b + 1 = 1", "variable": "b"},
        {"equation": "12*x = 0", "variable": "x"},
        {"equation": "31*y + 21 = 79", "variable": "y"},
        {"equation": "5*x = 200", "variable": "x"},
        {"equation": "-8*a = -42", "variable": "a"},
        {"equation": "6*b = 32", "variable": "b"},
        {"equation": "7*z - 21 = 0", "variable": "z"},
    ],
    "Difícil": [
        {"equation": "9*(x + 1) - 2 = 18", "variable": "x"},
        {"equation": "5*(3 - y) + 2*(y + 1) = -y + 5", "variable": "y"},
        {"equation": "5*(2 - z) = 2*(2 + z)", "variable": "z"},
        {"equation": "7*(1 + a) = 2*(-1 - a)", "variable": "a"},
        {"equation": "12*(5 + 32) = 12*b", "variable": "b"},
        {"equation": "10/2 + 3*x = (4*(2 + x)) / 2", "variable": "x"},
        {"equation": "9*(3 + y) - 72 = 27", "variable": "y"},
        {"equation": "3*(z + 2) = 3 - z + 2*(8 - z)", "variable": "z"},
        {"equation": "12*a / 2 = 3*(5 + a)", "variable": "a"},
        {"equation": "45*(3 + b) = -3*(-2 - b)", "variable": "b"},
    ]
}

def set_new_problem(equation: str, variable: str, difficulty: int):
    st.session_state.current_problem = equation
    st.session_state.solve_for = variable
    st.session_state.solution_steps = solver.get_equation_solve_steps(st.session_state.current_problem)
    st.session_state.hint_pos = 0
    st.session_state.problem_difficulty = difficulty

def set_random_problem():
    difficult = random.randint(1, 3)

    map_difficult = {
        1: "Fácil",
        2: "Médio",
        3: "Difícil"
    }

    problem = random.choice(equation_sets[map_difficult[difficult]])

    st.session_state.current_problem = problem['equation']
    st.session_state.solve_for = problem['variable']
    st.session_state.solution_steps = solver.get_equation_solve_steps(st.session_state.current_problem)
    st.session_state.hint_pos = 0
    st.session_state.problem_difficulty = difficult

# Interface Streamlit
st.title("Problemas de Equações Lineares")

nivel = st.selectbox("Escolha a dificuldade:", options=list(equation_sets.keys()))

st.subheader(f"Equações nível {nivel}")

for i, item in enumerate(equation_sets[nivel]):
    with st.container(border=True):
        st.markdown(f"**Equação:**")
        st.markdown(f"#### {item['equation']}")
        st.caption(f"**Resolva para:** `{item['variable']}`")

        if st.button("Resolver", key=i):
            map_difficult_to_int = {
                "Fácil": 1,
                "Médio": 2,
                "Difícil": 3
            }

            set_new_problem(item['equation'], item['variable'], map_difficult_to_int[nivel])

            st.switch_page("pages/main_page.py")


