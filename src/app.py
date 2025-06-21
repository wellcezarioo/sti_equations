# TODO: Use Case 01: Evaluate a equation and give the step by step solution with a GUI

import multiprocessing

from langchain_community.chat_models import ChatLlamaCpp
from langchain_core.messages import HumanMessage, SystemMessage
from llama_cpp import Llama


MODEL_PATH = "models/Gemma-3-Gaia-PT-BR-4b-it.i1-Q4_K_M.gguf"

def main():
    model = ChatLlamaCpp(
        model_path=MODEL_PATH,
    )

    messages = [
        SystemMessage("Traduza o seguinte texto do Inglês para o Português:"),
        HumanMessage("hello, how are you!"),
    ]

    response = model.invoke(messages)

    print(response.content)

if __name__ == "__main__":
    main() 
    