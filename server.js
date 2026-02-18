const express = require("express");
const cors = require("cors");
const multer = require("multer");
const axios = require("axios");
const fs = require("fs");
const path = require("path");
const FormData = require("form-data");

const app = express();
const upload = multer({ dest: "uploads/" });

app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {
  res.send("Node backend running");
});

app.post("/send_audio", upload.single("file"), async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ error: "No audio file uploaded" });
    }

    const audioPath = path.join(__dirname, req.file.path);

    const formData = new FormData();
    formData.append("file", fs.createReadStream(audioPath));

    const FASTAPI_URL = process.env.FASTAPI_URL || "http://localhost:8000";

    const fastApiResponse = await axios.post(
      `${FASTAPI_URL}/process_audio`,
      formData,
      { headers: formData.getHeaders() }
    );

    fs.unlinkSync(audioPath);

    return res.json({
      transcription: fastApiResponse.data.transcription,
      emotion: fastApiResponse.data.emotion,
      reply: `Detected emotion is ${fastApiResponse.data.emotion}, and you said "${fastApiResponse.data.transcription}".`
    });

  } catch (error) {
    console.error("ERROR in /send_audio:", error);
    return res.status(500).json({ error: "Failed to process audio" });
  }
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => console.log(`Node backend running on port ${PORT}`));
