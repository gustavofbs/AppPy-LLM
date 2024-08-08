from abc import ABC, abstractmethod
from transformers import pipeline

# Interface para Estratégia de Avaliação
class EvaluationStrategy(ABC):
    @abstractmethod
    def evaluate(self, response: str) -> dict:
        pass

class EmotionEvaluationStrategy(EvaluationStrategy):
    def __init__(self):
        # Carregando o pipeline com o modelo de classificação de emoções
        self.emotion_pipeline = pipeline('text-classification', model='michellejieli/emotion_text_classifier')

    def evaluate(self, response: str) -> dict:
        result = self.emotion_pipeline(response)
        emotion = result[0]['label']  # Rótulo da emoção mais provável
        confidence = result[0]['score']  # Pontuação de confiança

        # Explicação simples baseada na pontuação
        explanation = f"A resposta foi classificada como '{emotion}' com uma confiança de {confidence:.2f}."
        
        # Retorna um dicionário com o rótulo e a explicação
        return {'emotion': emotion, 'explanation': explanation}