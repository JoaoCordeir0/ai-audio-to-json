import os
from google import genai
from google.genai import types

class GeminiService:

    api_key = None

    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        
    def call_llm_api(self, system_message, user_message) -> str:
        client = genai.Client(api_key=self.api_key)

        user_message = f'Texto: [{user_message}]'
        
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            config=types.GenerateContentConfig(
                system_instruction=system_message,
                max_output_tokens=1000
            ),
            contents=user_message
        )
        
        try:
            return response.text.replace('```json', '').replace('```', '').strip()
        except Exception as e:
            raise Exception(f'Error: {e}')