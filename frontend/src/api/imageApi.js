import axios from "axios";

export const generateImage = async (prompt) => {
  try {
    const response = await axios.get("http://localhost:8000/generate/", {
      params: { prompt },
    });
    return response.data.url;
  } catch (error) {
    console.error("Error generating image:", error);
    alert("Failed to generate image. Try again.");
    return "";
  }
};
