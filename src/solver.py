"""
This module implements a wrapper of mathsteps library in /ext/js/
"""
import subprocess
from sympy import *

MATHSTEPS_LIBRARY_PATH = './ext/js/mathsteps/index.js'

def get_equation_solve_steps(equation: str):
    result = subprocess.run(["node", f"{MATHSTEPS_LIBRARY_PATH}", f"{equation}"], capture_output=True, text=True)

    print(result.stdout)

    return result.stdout

def get_equation_solution(equation: str, variable: str):
    x = symbols(variable)
    lhs_str, rhs_str = equation.split("=")
    lhs = sympify(lhs_str)
    rhs = sympify(rhs_str)

    eq = Eq(lhs, rhs)

    res = solve(eq, x)

    return res[0]

if __name__ == "__main__":
    print(get_equation_solve_steps("2*x + 3 = 7"))
    print(get_equation_solution("2*x + 3 = 7", 'x'))

