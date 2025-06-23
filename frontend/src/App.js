import React, { useState } from "react";
import { generateImage } from "./api/imageApi";

function App() {
  const [prompt, setPrompt] = useState("");
  const [imageUrl, setImageUrl] = useState("");

  const handleGenerate = async () => {
    const url = await generateImage(prompt);
    setImageUrl(url);
  };

  return (
    <div className="app-container">
      <h1>🖼️ AI Image Generator</h1>
      <input
        type="text"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter your image prompt"
        className="prompt-input"
      />
      <button onClick={handleGenerate} className="generate-btn">
        Generate
      </button>

      {imageUrl && (
        <div className="image-container">
          <h3>Generated Image:</h3>
          <img src={imageUrl} alt="Generated result" />
        </div>
      )}
    </div>
  );
}

export default App;
