from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.core.middleware import add_cors

# Import your routers
from app.api import image_gen
from app.api import auth_api  # JWT routes

# Import your database and models
from app.core.database import Base, engine
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Create the database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Apply CORS
add_cors(app)

# Include API routers
app.include_router(image_gen.router)
app.include_router(auth_api.router)

# Mount frontend folder
app.mount("/", StaticFiles(directory="../frontend/src", html=True), name="frontend")

# Favicon route
@app.get("/favicon.ico")
def favicon():
    return FileResponse("path/to/favicon.ico")
