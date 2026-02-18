const express = require('express');
const router = express.Router();
const axios = require('axios');

router.post('/message', async (req, res) => {
    const { text, audio } = req.body;
    try {
        // Send audio to FastAPI for emotion detection
        const emotionResp = await axios.post('http://127.0.0.1:8000/predict_emotion/', audio, {
            headers: { 'Content-Type': 'application/octet-stream' },
        });
        const emotion = emotionResp.data.emotion;

        let reply = "I see.";
        if(emotion === "happy") reply = "Glad to hear that! 😄";
        else if(emotion === "sad") reply = "Oh no, I'm here for you. 😢";
        else if(emotion === "angry") reply = "I understand your frustration. 😠";

        res.json({ reply });
    } catch(e) {
        res.json({ reply: "Error fetching emotion.", error: e.message });
    }
});
module.exports = router;
