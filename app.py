from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from google.cloud import speech
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Set GOOGLE_APPLICATION_CREDENTIALS to your service account key JSON
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "voice-bot-key.json"

@app.post("/send_audio")
async def send_audio(file: UploadFile = File(...)):
    content = await file.read()
    filename = "temp_audio.wav"
    with open(filename, "wb") as f:
        f.write(content)

    # Initialize client
    client = speech.SpeechClient()
    
    with open(filename, "rb") as audio_file:
        audio = speech.RecognitionAudio(content=audio_file.read())
    
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US"
    )

    # Detect speech
    response = client.recognize(config=config, audio=audio)

    # Extract transcription
    transcript = " ".join([result.alternatives[0].transcript for result in response.results])

    # Simple emotion detection mock (can later improve)
    emotions = ["happy", "sad", "angry", "calm"]
    import random
    detected_emotion = random.choice(emotions)

    os.remove(filename)
    return {"transcription": transcript, "emotion": detected_emotion}
