const express = require('express');
const path = require('path');
const axios = require('axios');
const { log } = require('console');

const app = express();
const PORT = 3000;

// Serve static files
app.use(express.static(path.join(__dirname, 'public')));

// Parse JSON body
app.use(express.json());

// Handle form submission
app.post('/submit', async (req, res) => {
  try {
    const response = await axios.post(
      'http://backend:5000/submit',
      req.body
    );

    res.json(response.data);
  } catch (error) {
    console.log(error);
    
    res.status(500).json({ error: 'Backend connection failed' });
  }
});

app.listen(PORT, () => {
  console.log(`Frontend running on http://localhost:${PORT}`);
});