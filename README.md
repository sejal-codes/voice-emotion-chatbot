Voice Emotion Chatbot

A voice-based emotion detection chatbot built with Python (Flask).
It detects emotions like happy, sad, neutral from voice input and responds accordingly.

Features

Upload a WAV or MP3 audio file.

Detects emotions using pitch and energy analysis.

Generates simple chatbot responses based on detected emotion.

Lightweight Flask backend with file upload support.

Optional: Can integrate with a frontend for live voice input.

How It Works

The user uploads a voice file (.wav or .mp3) via the /chat endpoint.

The backend:

Converts MP3 to WAV if needed.

Extracts audio features using librosa.

Classifies emotion using a simple pitch + energy-based algorithm.

Returns a JSON response with:

{
  "emotion": "happy",
  "response": "You sound happy! Keep smiling 😄",
  "transcript": ""
}

Requirements

Python 3.9+

Flask

Flask-CORS

NumPy

librosa

pydub

Install dependencies with:

pip3 install -r requirements.txt


⚠️ Note: For MP3 support, you need ffmpeg installed. On macOS, consider using MacPorts since Homebrew may not work on older versions.

Usage

Start the backend server:

python3 app.py


Send a test audio:

curl -X POST -F "audio=@test_audio.wav" http://127.0.0.1:5000/chat


You’ll get a JSON response with the detected emotion and chatbot reply.

Project Structure
voice_emotion_chatbot/
│
├── app.py                # Flask backend
├── emotion_module.py     # Emotion detection logic
├── requirements.txt      # Dependencies
├── README.md
└── uploads/              # Folder to store uploaded files

Future Improvements (Optional)

Live microphone input in the frontend.

More advanced emotion detection using ML models.

Multi-language support for speech-to-text.

Author

Sejal Solanki | First-year CS student | Portfolio-ready backend project
