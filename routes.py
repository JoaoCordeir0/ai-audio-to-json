from fastapi import APIRouter, Depends
from src.middleware.OAuth import OAuth
from src.models.AudioToJsonModel import AudioToJsonModel
from src.controllers.AudioToJsonController import AudioToJsonController

router = APIRouter(prefix='/api')

""" NOTE: Rotas get da API -> """
@router.get('/health')
def main():
    return 'ok'

""" NOTE: Rotas post da API -> """
@router.post('/audio-to-json')
def product_audio_to_json(params: AudioToJsonModel = Depends(AudioToJsonModel.get_form)):
    return AudioToJsonController(params).audio_to_json()