"""
This module implements a wrapper of mathsteps library in /ext/js/
"""
import subprocess

MATHSTEPS_LIBRARY_PATH = './ext/js/mathsteps/index.js'

def get_equation_solve_steps(equation: str):
    result = subprocess.run(["node", f"{MATHSTEPS_LIBRARY_PATH}", f"{equation}"], capture_output=True, text=True)

    print(result.stdout)

    return result.stdout