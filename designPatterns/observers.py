# designPatterns/observer.py

from abc import ABC, abstractmethod

# Interface Observer
class Observer(ABC):
    @abstractmethod
    def update(self, response: str, emotion: str, explanation: str):
        pass

# Interface Observable
class Observable(ABC):
    def __init__(self):
        self._observers = []

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self, response: str, emotion: str, explanation: str):
        for observer in self._observers:
            observer.update(response, emotion, explanation)

# Implementação de um Observer para CLI
class CLIObserver(Observer):
    def __init__(self):
        self.first_update = True  # Controle para a primeira atualização

    def update(self, response: str, emotion: str, explanation: str):
        if not self.first_update:
            print("\nAtualização Detectada!")
        else:
            self.first_update = False

        print(f"Nova Resposta: {response}")
        print(f"Intenção Atualizada: {emotion}")
        print(f"Explicação: {explanation}")
        print("\n")
