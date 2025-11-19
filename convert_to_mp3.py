from pydub import AudioSegment

# Load your WAV file
sound = AudioSegment.from_wav("test_audio.wav")

# Export as MP3
sound.export("test_audio.mp3", format="mp3")
print("✅ test_audio.mp3 created!")
