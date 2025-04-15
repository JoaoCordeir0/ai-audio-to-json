import whisper
from faster_whisper import WhisperModel
import speech_recognition as sr

class AudioToTextService:

    def __init__(self):
        pass
    
    def transcribe_audio_whisper(self, audio_path):
        model = whisper.load_model('medium') # ou 'small', 'large', etc.
        result = model.transcribe(audio_path)
        return result['text']

    def transcribe_audio_faster_whisper(self, audio_path):
        model = WhisperModel("base", compute_type="int8")
        segments, _ = model.transcribe(audio_path)
        text = "".join([seg.text for seg in segments])
        return text
    
    def transcribe_audio_google(self, audio_path):
        r = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = r.record(source)
        text = r.recognize_google(audio, language='pt-BR')
        return text