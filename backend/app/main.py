from fastapi import FastAPI
from .core.config import add_cors
from .api import image_gen

app = FastAPI()

# Add CORS for frontend connection
add_cors(app)

# Include API router
app.include_router(image_gen.router)
