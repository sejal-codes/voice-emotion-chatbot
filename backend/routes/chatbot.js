const express = require('express');
const router = express.Router();

// POST /api/chatbot/message
router.post('/message', (req, res) => {
    const { text, emotion } = req.body;

    let reply = "I see.";

    if (emotion === "happy") reply = "Glad to hear that! 😄";
    else if (emotion === "sad") reply = "Oh no, I'm here for you. 😢";
    else if (emotion === "angry") reply = "I understand your frustration. 😠";
    else reply = "Got it!";

    res.json({ reply });
});

module.exports = router;
