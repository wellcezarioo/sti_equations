# 📚 Resolvedor de Equações de Primeiro Grau com Explicações em Linguagem Natural

Este projeto é uma prova de conceito de um Sistema Tutor Inteligente (STI) que integra:

- Um **resolvedor simbólico** de equações de 1º grau (`mathsteps`);
- Uma **LLM (Large Language Model)** local usando `Ollama`;
- Um componente Python que realiza o pipeline:
  - Extrai a equação de uma pergunta feita por um aluno;
  - Resolve a equação com `mathsteps`;
  - Reescreve os passos da resolução em linguagem natural.

---

## 🛠 Pré-requisitos

### Python

- Python 3.10 ou superior
- `pip` para instalar dependências

### Node.js

- Node.js 18+ (necessário para executar o `mathsteps`)

---

## 📦 Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instalar dependências Python
```bash
pip install -r requirements.txt
```

### 3. Instalar dependências do mathsteps
Entre na pasta ext/js/mathsteps e instale os pacotes Node.js:
```bash
cd ext/js/mathsteps
npm install
```

Essa etapa é necessária porque o módulo solver.py usa o mathsteps via node para resolver equações.

### 4. Volte para a raiz do projeto:
```bash
cd ../../../
```

### 5. Instale o Ollama
https://ollama.com/download

---

## 🚀 Execução

Certifique-se de que o modelo Ollama (gemma3, por padrão) está disponível localmente executando:

```bash
ollama run gemma3
```

Execute o script principal com:
```bash
python src/app.py
```

Isso irá:
- Usar a LLM para extrair a equação de uma pergunta em linguagem natural;
- Resolver a equação com mathsteps;
- Reescrever os passos da resolução em uma explicação mais amigável ao aluno.

---

### 📚 Referências
- Mathsteps — Biblioteca open-source da Google para resolução simbólica de equações matemáticas.
- Ollama — Plataforma para executar modelos LLM localmente.
- LangChain — Framework para encadeamento de modelos de linguagem.