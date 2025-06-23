from fastapi import APIRouter
from typing import Optional
import openai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

router = APIRouter()

@router.get("/generate/")
def generate_image(prompt: Optional[str] = "A random image"):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        return {"url": image_url}
    except Exception as e:
        return {"error": str(e)}
