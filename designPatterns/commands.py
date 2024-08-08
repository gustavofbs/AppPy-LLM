from abc import ABC, abstractmethod
from .factory import LLMClient
from .observers import Observable

# Padrão Command para encapsular solicitações
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class GenerateResponseCommand(Command, Observable):
    def __init__(self, client: LLMClient, prompt: str):
        Command.__init__(self)
        Observable.__init__(self)  # Inicializa a parte Observable
        self.client = client
        self.prompt = prompt
        self.response = None
        self.emotion = None
        self.explanation = None

    def execute(self):
        self.response = self.client.generate_response(self.prompt)
        return self.response

    def set_emotion(self, emotion: str, explanation: str):
        self.emotion = emotion
        self.explanation = explanation
        # Agora notifica os observadores com a resposta, emoção e explicação
        self.notify_observers(self.response, self.emotion, self.explanation)


