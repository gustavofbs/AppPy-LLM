from abc import ABC, abstractmethod
import os
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai as genai

class LLMClient(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        pass

class ChatGPTClient(LLMClient):
    def __init__(self):
        load_dotenv()
        self.organization = os.getenv('ORGANIZATION_ID')
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.project = os.getenv('PROJECT_ID')

        self.client = OpenAI(
            organization=self.organization,
            api_key=self.api_key,
            project=self.project
        )

    def generate_response(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        message_content = response.choices[0].message.content
        return message_content

class PalmClient(LLMClient):
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('PALM_API_KEY')
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_response(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text
        
class LLMFactory:
    @staticmethod
    def create_client(client_type: str) -> LLMClient:
        if client_type == 'chatgpt':
            return ChatGPTClient()
        elif client_type == 'palm':
            return PalmClient()
        else:
            raise ValueError(f"Unknown client type: {client_type}")
