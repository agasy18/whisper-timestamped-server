from typing import Union
from fastapi import FastAPI, UploadFile
import whisper_timestamped as whisper
from pydantic import BaseModel
from os import getenv
from tempfile import NamedTemporaryFile
from tqdm import tqdm

app = FastAPI()

model = whisper.load_model(getenv('MODEL') or "small", device=getenv('DEVICE') or "cuda")

@app.post("/transcribe")
async def get_whisper_result(audio: UploadFile, language: str = 'auto', refine_whisper_precision: float=0.7):
    
    with NamedTemporaryFile() as f:
        with tqdm(total=audio.size, desc='Featching file') as pbar:
            while content := await audio.read(1024):
                f.write(content)
                pbar.update(len(content))
        f.seek(0)
        arr = whisper.load_audio(f.name)
    
    if language == 'auto':
        language = None

    result = whisper.transcribe(model, arr, language=language, refine_whisper_precision=refine_whisper_precision)
    return result