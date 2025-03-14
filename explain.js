// src/api/explain.js
const express = require('express');
const router = express.Router();

// Dummy explanation generator function
function getModelExplanation(inputText) {
  // In production, call your Python script or model here.
  return {
    explanation: `The model predicts that the input "${inputText}" is influenced most by feature X and feature Y.`,
    featureImportance: { featureX: 0.65, featureY: 0.35 }
  };
}

router.post('/explain', (req, res) => {
  const { inputText } = req.body;
  if (!inputText) {
    return res.status(400).json({ error: 'Input text is required for explanation.' });
  }
  const explanationResult = getModelExplanation(inputText);
  res.json(explanationResult);
});

module.exports = router;
