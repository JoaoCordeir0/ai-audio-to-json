from openai import AzureOpenAI
import os
from src.utils.PromptUtil import PromptUtil

class OpenAIService:

    api_key = None
    api_version = None
    azure_endpoint = None

    def __init__(self) -> None:
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.api_version = os.getenv('OPENAI_API_VERSION')
        self.azure_endpoint = os.getenv('OPENAI_API_ENDPOINT')
        
    def call_openai_api(self, system_message, user_message):                
        client = AzureOpenAI(
            api_key=self.api_key,
            api_version=self.api_version,
            azure_endpoint=self.azure_endpoint
        )

        try:
            user_message = f'Texto: [{user_message}]'

            response = client.chat.completions.create(
                model='gpt-4o',
                messages=[
                    {'role': 'system', 'content': system_message},
                    {'role': 'user', 'content': user_message}
                ]
            )
            return response.choices[0].message.content.strip().replace('```json', '').replace('```', '')
        except Exception as e:        
            raise Exception(f'Error: {e}')