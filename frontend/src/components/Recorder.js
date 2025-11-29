import React, { useState } from 'react';
import axios from 'axios';

function Recorder() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");

  const handleSend = async () => {
    try {
      const emotion = "happy"; // placeholder
      const res = await axios.post("http://localhost:5000/api/chatbot/message", { text: message, emotion });
      setReply(res.data.reply);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <input 
        type="text" 
        placeholder="Type a message..." 
        value={message} 
        onChange={(e) => setMessage(e.target.value)} 
        style={{ width: '300px', padding: '10px' }}
      />
      <button onClick={handleSend} style={{ padding: '10px', marginLeft: '10px' }}>Send</button>
      <div style={{ marginTop: '20px' }}>
        <strong>Reply:</strong> {reply}
      </div>
    </div>
  );
}

export default Recorder;
