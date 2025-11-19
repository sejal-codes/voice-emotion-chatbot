🎤 Voice Emotion Chatbot

A voice-based emotion detection chatbot built with Python (Flask). Upload your voice, and it detects emotions like happy, sad, or neutral, then responds naturally. Perfect portfolio-ready backend project for beginners.

🚀 Features

🎧 Upload WAV or MP3 audio files.

🧠 Detect emotions using pitch & energy analysis.

💬 Generates chatbot responses based on emotion.

⚡ Lightweight Flask backend with file upload support.

🌐 Optional: Integrates with a frontend for live voice input.

🧩 How It Works

User uploads a voice file via /chat endpoint.

Backend processes the file:

Converts MP3 → WAV if needed.

Extracts audio features using librosa.

Classifies emotion with a pitch + energy-based algorithm.

Returns JSON response like:

{
  "emotion": "happy",
  "response": "You sound happy! Keep smiling 😄",
  "transcript": ""
}

⚙️ Requirements

Python 3.9+

Libraries: Flask, Flask-CORS, NumPy, librosa, pydub

💡 Tip: For MP3 support, install ffmpeg. On macOS older versions, MacPorts
 may be needed.

Install dependencies:

pip3 install -r requirements.txt

📝 Usage

Start backend server:

python3 app.py


Send a test audio file:

curl -X POST -F "audio=@test_audio.wav" http://127.0.0.1:5000/chat
