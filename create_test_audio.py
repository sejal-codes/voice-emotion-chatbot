# create_test_audio.py
import numpy as np
import soundfile as sf

sr = 22050  # sample rate
t = np.linspace(0, 1, sr)
y = 0.5 * np.sin(2 * np.pi * 440 * t)  # 440Hz sine wave

sf.write('test_audio.wav', y, sr)
print("✅ test_audio.wav created!")

