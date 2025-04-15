from pydantic import BaseModel
from fastapi import File, UploadFile, Form

class AudioToJsonModel(BaseModel):

    type: str = Form("")
    audio: UploadFile = File(...)

    @staticmethod
    def get_form(type: str = Form(""), audio: UploadFile = File(...)):
        return AudioToJsonModel(type=type, audio=audio)