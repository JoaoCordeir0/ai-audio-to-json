import os
from pydub import AudioSegment

class FileUtil:

    @staticmethod
    def save_tmp_audio(file) -> str:
        if not file or file.filename == '':
            return None
        
        path = os.path.join('tmp', file.filename)

        with open(path, 'wb') as f:
            f.write(file.file.read())
        
        wav = path.replace("mp3", "wav")
        audio = AudioSegment.from_mp3(path)
        audio.export(wav, format="wav")

        return wav

    @staticmethod
    def delete_tmp_files() -> None:
        dir = os.listdir('tmp/')
        for file in dir:
            os.remove(f'tmp/{file}')