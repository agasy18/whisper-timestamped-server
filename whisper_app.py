from fastapi import FastAPI
import whisper_timestamped as whisper
from pydantic import BaseModel

app = FastAPI()

class TranscriptionRequest(BaseModel):
    audio_file: str
    language: str


@app.post("/whisper")
async def get_whisper_result(request: TranscriptionRequest):
    audio = whisper.load_audio(request.audio_file)
    model = whisper.load_model("tiny", device="cpu")
    result = whisper.transcribe(model, audio, language=request.language)
    return result