# TODO: Use Case 01: Evaluate a equation and give the step by step solution with a GUI

import asyncio
import multiprocessing
import subprocess

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
from llama_cpp import Llama


MODEL_PATH = "models/Gemma-3-Gaia-PT-BR-4b-it.i1-Q4_K_M.gguf"
MODEL_NAME = "gemma3"

REWRITE_STEPS_PROMPT = """
Você é um sistema especialista em equações de primeiro grau. Abaixo está um passo a passo da resolução de uma equação:

{mathsteps}

Sua tarefa é reescrever esse processo de forma mais natural.
"""

EXTRACT_EQUATION_PROMPT = """
Você é um sistema especialista em equações de primeiro grau.
Abaixo está a mensagem de um aluno. Sua tarefa é:

Identificar e extrair apenas a equação de primeiro grau contida na mensagem.

Use ponto (.) como separador decimal — não use vírgulas.

Não adicione explicações, comentários ou qualquer texto além da equação.

Mensagem do aluno:
{user_message}
"""

async def rewrite_steps():
    model = ChatOllama(model=MODEL_NAME, temperature=0.1)

    prompt_template = PromptTemplate.from_template(REWRITE_STEPS_PROMPT)

    chain = prompt_template | model

    response = chain.astream({"mathsteps": test_solve("2x + 3x + 1.5x + 3.2x = 35.7")})

    async for token in response:
        print(token.content, end="", flush=True)

def test_solve(equation: str):
    result = subprocess.run(["node", "ext/js/index.js", f"{equation}"], capture_output=True, text=True)

    print(result.stdout)
    
    return result.stdout

async def extract_equations(user_message: str):
    model = ChatOllama(model=MODEL_NAME, temperature=0.1)

    prompt_template = PromptTemplate.from_template(EXTRACT_EQUATION_PROMPT)

    chain = prompt_template | model

    response = chain.astream({"user_message": user_message})

    async for token in response:
        print(token.content, end="", flush=True)
        
    print("")
    
async def extract_and_solve(user_message: str):
    model = ChatOllama(model=MODEL_NAME)

    prompt_template_extract = PromptTemplate.from_template(EXTRACT_EQUATION_PROMPT)
    chain_extract = prompt_template_extract | model
    response_extract = chain_extract.invoke({"user_message": user_message})
    print(response_extract.content)
    
    prompt_template_solve = PromptTemplate.from_template(REWRITE_STEPS_PROMPT)
    chain_solve = prompt_template_solve | model

    response = chain_solve.astream({"mathsteps": test_solve(response_extract.content)})
    
    async for token in response:
        print(token.content, end="", flush=True)
        
    print("")
    


if __name__ == "__main__":
    # asyncio.run(rewrite_steps())
    
    user_message = """
    Como que eu resolvo a equação:
    
    2x + 3x + 1.5x + 3.2x = 35.7 
    
    ? Me ajuda por favor!!!
    """
    
    # asyncio.run(extract_equations(user_message))
    
    asyncio.run(extract_and_solve(user_message))
    