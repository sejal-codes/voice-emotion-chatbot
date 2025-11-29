const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const chatbotRoute = require('./routes/chatbot');

const app = express();
const PORT = 5000;

app.use(cors());
app.use(bodyParser.json());

// Routes
app.use('/api/chatbot', chatbotRoute);

app.get('/', (req, res) => {
    res.send('Voice Emotion Chatbot Backend Running');
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
