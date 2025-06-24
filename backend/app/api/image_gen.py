from fastapi import APIRouter
from fastapi.responses import JSONResponse
import requests
import uuid
import os
import base64

router = APIRouter()

@router.get("/generate/")
def generate_image(prompt: str):
    API_KEY = "sk-Ob2FKAowDSQ22oq9obQEzcLSPnEDIl3Hgya8wYraFKy3z9xC"
    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    payload = {
        "text_prompts": [{"text": prompt}],
        "cfg_scale": 7,
        "height": 1024,
        "width": 1024,
        "samples": 1,
        "steps": 30
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    image_data = data["artifacts"][0]["base64"]

    # Ensure the directory exists
    os.makedirs("generated_images", exist_ok=True)

    filename = f"{uuid.uuid4()}.png"
    file_path = f"generated_images/{filename}"

    with open(file_path, "wb") as f:
        f.write(base64.b64decode(image_data))

    image_url = f"http://localhost:8000/images/{filename}"
    return JSONResponse(content={"url": image_url})
