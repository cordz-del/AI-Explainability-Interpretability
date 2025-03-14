// src/components/ExplanationDisplay.jsx
import React, { useEffect, useState } from 'react';

const ExplanationDisplay = () => {
  const [explanationImage, setExplanationImage] = useState(null);

  useEffect(() => {
    async function fetchExplanation() {
      try {
        const response = await fetch('https://your-backend-api.com/api/explain', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ inputText: "I'm worried about my exam." })
        });
        const data = await response.json();
        // Assume the API returns a base64 encoded image for the SHAP plot.
        setExplanationImage(`data:image/png;base64,${data.shapPlot}`);
      } catch (error) {
        console.error("Error fetching explanation:", error);
      }
    }
    fetchExplanation();
  }, []);

  return (
    <div>
      <h3>Model Explanation</h3>
      {explanationImage ? (
        <img src={explanationImage} alt="SHAP Summary Plot" style={{ maxWidth: '100%' }} />
      ) : (
        <p>Loading explanation...</p>
      )}
    </div>
  );
};

export default ExplanationDisplay;
