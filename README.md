🎙 Voice Emotion Detection Chatbot

An AI-powered Voice Emotion Detection Chatbot that analyzes user voice input, detects emotional tone, and generates an empathetic response. This project combines speech processing, backend integration, and AI concepts to improve human–computer interaction.


---

🚀 Project Overview

This system allows users to record their voice through a web interface. The audio is processed using a FastAPI backend integrated with Google Cloud Speech-to-Text for transcription. A basic emotion detection logic is applied, and the chatbot generates a contextual reply based on the detected emotion.

The goal of this project is to bridge the emotional gap in traditional chatbots by making them emotion-aware.


---

🏗 System Architecture

Frontend (HTML + JS + Web Audio API)
⬇
Node.js Backend (Express + Multer + Axios)
⬇
FastAPI Service (Python)
⬇
Google Cloud Speech-to-Text API
⬇
Emotion Detection + Chatbot Response


---

📂 Project Structure

├── server.js          # Node.js backend server
├── chatbot.js         # Chatbot route logic
├── package.json       # Node dependencies
├── index.html         # Frontend interface
├── app.py             # FastAPI backend (Speech + Emotion)
└── uploads/           # Temporary audio storage


---

🛠 Tech Stack

Frontend:

HTML5

CSS3

JavaScript

Web Audio API

MediaRecorder API


Backend:

Node.js

Express.js

Multer (file upload)

Axios


AI / Processing:

FastAPI (Python)

Google Cloud Speech-to-Text

Basic emotion classification logic



---

⚙ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/your-username/voice-emotion-chatbot.git
cd voice-emotion-chatbot


---

2️⃣ Setup Node Backend

npm install
npm start

Runs on:

http://localhost:8080


---

3️⃣ Setup FastAPI Backend

Install dependencies:

pip install fastapi uvicorn google-cloud-speech python-multipart

Run server:

uvicorn app:app --reload --port 8000

Runs on:

http://localhost:8000


---

4️⃣ Google Cloud Setup

Create a Google Cloud project

Enable Speech-to-Text API

Create a Service Account Key (JSON)

Download the key and rename it:


voice-bot-key.json

Set environment variable:

export GOOGLE_APPLICATION_CREDENTIALS="voice-bot-key.json"

(For Windows: use set instead of export)


---

🎯 Features

🎤 Real-time voice recording

🌊 Live waveform visualization

📝 Speech-to-text transcription

😊 Emotion detection (happy, sad, angry, calm)

🤖 Emotion-aware chatbot replies

🌐 CORS-enabled API communication



---

🧠 How It Works

1. User records voice from browser.


2. Audio is sent to Node backend.


3. Node forwards audio to FastAPI service.


4. FastAPI uses Google Speech API to transcribe speech.


5. Emotion is detected (mock/random logic currently).


6. Chatbot generates an empathetic response.


7. Result is displayed on frontend.




---

📊 Current Limitations

Emotion detection uses mock/random logic (not ML-based yet).

Limited emotion categories.

Background noise can affect transcription accuracy.

No persistent database integration.



---

🔮 Future Improvements

Integrate real ML-based emotion classification (e.g., MFCC + Deep Learning).

Deploy using Docker + Cloud hosting (AWS/GCP).

Add user authentication and conversation history.

Improve real-time streaming analysis.

Expand multilingual support.



---

🎓 Academic Context

Developed as part of an Innovation & Design Thinking Project, applying empathy-driven problem solving to build an emotion-aware AI system.


---

👩‍💻 Author

Sejal Solanki
Computer Science Undergraduate
Cloud & AI/ML Enthusiast


---

📜 License

This project is for educational and research purposes.


---
