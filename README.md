🎤 Voice Emotion Chatbot




A voice-based emotion detection chatbot built with Python (Flask). Upload your WAV audio, and it detects emotions like happy, sad, or neutral, then responds naturally.
Perfect portfolio-ready backend project for beginners.


____________________________________________

🚀 Features




🎧 Upload WAV audio files.

🧠 Detect emotions using pitch & energy analysis.

💬 Generates chatbot responses based on detected emotion.

⚡ Lightweight Flask backend with file upload support.

🌐 Optional: Can integrate with a frontend for live voice input.



_______________________________________________
🧩 How It Works



1. User uploads a WAV file via /chat endpoint.


2. Backend processes the file:

Extracts audio features using librosa.

Classifies emotion with a simple pitch + energy-based algorithm.



3. Returns JSON response like:



{
  "emotion": "happy",
  "response": "You sound happy! Keep smiling 😄",
  "transcript": ""
}


_______________________________________________

⚙️ Requirements




Python 3.9+

Libraries: Flask, Flask-CORS, NumPy, librosa, pydub


Install dependencies:

pip3 install -r requirements.txt

⚠️ Note: Currently, only WAV files are supported. MP3 support requires ffmpeg installation, which is not included due to system limitations.


______________________________________________

📝 Usage




1. Start backend server:



python3 app.py

2. Send a test audio file:



curl -X POST -F "audio=@test_audio.wav" http://127.0.0.1:5000/chat

3. You’ll get a JSON response with detected emotion and chatbot reply.




______________________________________________

📂 Project Structure




voice_emotion_chatbot/
├── app.py              # Flask backend
├── emotion_module.py   # Emotion detection logic
├── requirements.txt    # Dependencies
├── README.md
└── uploads/            # Uploaded WAV files


______________________________________________

🌟 Future Improvements (Optional)




🎤 Live microphone input in frontend.

🤖 Advanced emotion detection using ML models.

🌍 Multi-language support for speech-to-text.



_______________________________________________

🖋 Author



Sejal Solanki | First-year CS student | Portfolio-ready backend project 



