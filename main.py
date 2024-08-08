from designPatterns.factory import LLMFactory
from designPatterns.commands import GenerateResponseCommand
from designPatterns.strategy import EmotionEvaluationStrategy
from designPatterns.observers import CLIObserver

# CLI para processar os comandos
def main():
    emotion_evaluation_strategy = EmotionEvaluationStrategy()
    cli_observer = CLIObserver()

    print(f"\nBem-vindo à interface de linha de comando de LLM!")
    print("\n")
    print(f"Escolha o cliente (chatgpt/palm) e insira sua pergunta.")
    print("\n")
    print("Digite 'Sair' para encerrar a aplicação a qualquer momento.")
    print("\n")

    while True:
        client_type = input("Cliente (chatgpt/palm): ").strip().lower()
        if client_type == 'sair':
            break
        if client_type not in ['chatgpt', 'palm']:
            print("Cliente inválido. Por favor, escolha 'chatgpt' ou 'palm'.")
            continue

        prompt = input("Pergunta: ").strip()
        if prompt.lower() == 'sair':
            break
        if not prompt:
            print("Pergunta inválida. Por favor, insira uma pergunta válida.")
            continue

        client = LLMFactory.create_client(client_type)
        command = GenerateResponseCommand(client, prompt)
        command.add_observer(cli_observer)
        
        response = command.execute()

        # Avaliação da Intenção e Geração da Explicação
        evaluation_result = emotion_evaluation_strategy.evaluate(response)
        emotion = evaluation_result['emotion']
        explanation = evaluation_result['explanation']

        command.set_emotion(emotion, explanation)  # Notifica os observadores uma vez com resposta, emoção e explicação

        # A resposta do cliente não será exibida diretamente

    print("Aplicação encerrada.")

if __name__ == "__main__":
    main()


