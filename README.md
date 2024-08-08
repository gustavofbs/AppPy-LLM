# LLM CLI Application

## Descrição

Esta é uma aplicação de linha de comando (CLI) para interagir com modelos de linguagem como ChatGPT (OpenAI) e PalmAPI (Gemini). A aplicação permite ao usuário enviar perguntas para o modelo selecionado e receber respostas analisadas por uma estratégia de avaliação de emoções. O projeto utiliza padrões de design como Factory, Command, Strategy e Observer para estruturar o código.

## Funcionalidades

- **Seleção de Cliente:** Escolha entre ChatGPT e Palm para gerar respostas.
- **Perguntas e Respostas:** Envie perguntas e receba respostas do modelo selecionado.
- **Avaliação de Emoções:** Analisa a emoção da resposta usando a biblioteca `transformers` com um modelo de classificação de texto pré-treinado. Este modelo é usado para identificar a emoção predominante na resposta.
- **Atualizações e Notificações:** Exibe atualizações sobre as respostas e emoções através de um observer.
- **Saída do Terminal:** Opção para encerrar a aplicação a qualquer momento.

## Estrutura do Projeto

- **`factory.py`**: Implementa o padrão Factory para criar instâncias de clientes de LLM.
- **`commands.py`**: Implementa o padrão Command para encapsular a geração de respostas.
- **`strategy.py`**: Define a estratégia de avaliação de emoções usando o padrão Strategy, com a biblioteca `transformers`
- **`observer.py`**: Implementa o padrão Observer para notificar sobre atualizações de respostas e emoções.
- **`main.py`**: Arquivo principal que executa a CLI e gerencia a interação com o usuário.

## Requisitos

Para que as LLM sejam usadas, é necessária adicionar um arquivo `.env` e adicionar os tokens relacionados a:
- `ORGANIZATION_ID`
- `OPENAI_API_KEY`
- `PROJECT_ID`
- `PALM_API_KEY`

## Instalação

1. Clone o repositório:
    ```bash
    git clone git@github.com:gustavofbs/AppPy-LLM.git
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    # Em sistemas Unix, use `source venv/bin/activate`  # No Windows, use `venv\Scripts\activate`
    ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Execute a aplicação:
    ```bash
    python main.py
    ```

2. Siga as instruções na CLI para escolher um cliente (chatgpt/palm) e inserir sua pergunta.

3. A aplicação exibirá as respostas e as emoções associadas, notificando sobre atualizações.

4. Para sair da aplicação, digite `Sair` a qualquer momento.
