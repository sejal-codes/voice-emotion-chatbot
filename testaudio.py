import numpy as np
import soundfile as sf

# Generate a 1-second sine wave at 440Hz (A4 note)
sr = 22050  # sample rate
t = np.linspace(0, 1, sr)
y = 0.5 * np.sin(2 * np.pi * 440 * t)

# Save as test_audio.wav in current folder
sf.write('test_audio.wav', y, sr)
print("test_audio.wav created!")
