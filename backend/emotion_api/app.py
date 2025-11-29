from fastapi import FastAPI, UploadFile, File
import numpy as np
import librosa
from sklearn.preprocessing import StandardScaler

app = FastAPI(title="Voice Emotion API")

@app.get("/")
def read_root():
    return {"message": "Voice Emotion API running!"}

@app.post("/predict_emotion/")
async def predict_emotion(file: UploadFile = File(...)):
    y, sr = librosa.load(file.file, sr=22050)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    features = np.mean(mfccs, axis=1)
    features = StandardScaler().fit_transform([features])

    # Placeholder prediction for now
    prediction = "happy"

    return {"emotion": prediction}
