import React, { useState } from "react";
import { generateImage } from "./api/imageApi";
import "./App.css";

function App() {
  const [prompt, setPrompt] = useState("");
  const [imageUrl, setImageUrl] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!prompt.trim()) {
      alert("Please enter a prompt!");
      return;
    }

    setLoading(true);
    const url = await generateImage(prompt);
    setImageUrl(url);
    setLoading(false);
  };

  return (
    <div className="app">
      <h1>🎨 AI Image Generator</h1>
      <div className="input-section">
        <input
          type="text"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Describe your dream image..."
        />
        <button onClick={handleGenerate}>Generate</button>
      </div>

      {loading && <div className="loader"></div>}

      {imageUrl && (
        <div className="image-card">
          <img src={imageUrl} alt="AI Generated" />
          <p>{prompt}</p>
        </div>
      )}

      <footer>Built with ❤️ by Madhu</footer>
    </div>
  );
}

export default App;
