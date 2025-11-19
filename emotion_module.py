import librosa
import numpy as np

def detect_emotion(audio_path):
    try:
        y, sr = librosa.load(audio_path)
        if y.size == 0:
            return "neutral"

        energy = np.mean(librosa.feature.rms(y=y))
        pitch = np.mean(librosa.yin(y, fmin=80, fmax=8000))

        if pitch > 200 and energy > 0.05:
            return "happy"
        elif pitch < 150 and energy < 0.03:
            return "sad"
        else:
            return "neutral"

    except Exception as e:
        print(f"[detect_emotion] Failed to process {audio_path}: {e}")
        return "neutral"
