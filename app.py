from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import logging
from emotion_module import detect_emotion
from pydub import AudioSegment

# --------------------------
# Setup
# --------------------------
app = Flask(__name__)
CORS(app)  # allow requests from frontend

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Logging setup
logging.basicConfig(level=logging.INFO)

# --------------------------
# Routes
# --------------------------
@app.route('/')
def home():
    return "Voice Emotion Chatbot Backend Running!"

# Unified /chat endpoint
@app.route('/chat', methods=['POST'])
def chat():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio']

    # Save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, audio_file.filename)
    audio_file.save(file_path)

    # Log received file
    logging.info("Received file: {}".format(audio_file.filename))

    # Convert MP3 to WAV if needed
    if file_path.lower().endswith('.mp3'):
        try:
            sound = AudioSegment.from_mp3(file_path)
            wav_path = file_path.rsplit('.', 1)[0] + '.wav'
            sound.export(wav_path, format="wav")
            file_path = wav_path
            logging.info("Converted MP3 to WAV: {}".format(wav_path))
        except Exception as e:
            logging.error(f"MP3 to WAV conversion failed: {str(e)}")
            return jsonify({"error": f"Failed to convert MP3 to WAV: {str(e)}"}), 500

    # Detect emotion
    try:
        emotion = detect_emotion(file_path)
        logging.info(f"Detected emotion: {emotion}")
    except Exception as e:
        logging.error(f"Emotion detection failed: {str(e)}")
        return jsonify({"error": f"Failed to detect emotion: {str(e)}"}), 500

    # Generate a simple contextual response
    response_text = ""
    if emotion == "happy":
        response_text = "You sound happy! Keep smiling 😄"
    elif emotion == "sad":
        response_text = "You sound a bit down. Hope things get better 💛"
    else:
        response_text = "You sound neutral. How's your day going?"

    # Return JSON
    return jsonify({
        "emotion": emotion,
        "response": response_text
    })

# --------------------------
# Run server
# --------------------------
if __name__ == "__main__":
    app.run(debug=True)
