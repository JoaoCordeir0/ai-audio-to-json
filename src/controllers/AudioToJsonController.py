from src.utils.FileUtil import FileUtil
from src.services.OpenAIService import OpenAIService
from src.services.AudioToTextService import AudioToTextService
from src.utils.PromptUtil import PromptUtil
import json

class AudioToJsonController:

    params = None

    def __init__(self, params) -> None:
        self.params = params

    def audio_to_json(self) -> dict:
        audio_path = FileUtil.save_tmp_audio(self.params.audio)
        
        audio_service = AudioToTextService()
        # text = audio_service.transcribe_audio_whisper(audio_path) # Excelente porém demorado
        # text = audio_service.transcribe_audio_faster_whisper(audio_path) # Rápido porém eficácia mediana 
        text = audio_service.transcribe_audio_google(audio_path) # Rápido e eficácia boa

        openai_service = OpenAIService()

        match self.params.type:
            case 'product-register':
                prompt = PromptUtil.get_prompt_product_register()
                result = openai_service.call_openai_api(prompt, text)
            case _:
                raise Exception('Not found type')
    
        FileUtil.delete_tmp_files()

        return {
            'audio_text': text,
            'product_info': json.loads(result)
        }
        