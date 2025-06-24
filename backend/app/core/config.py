import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.env'))

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))  # Default 30 mins if not set

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL is not set in the .env file")
if SECRET_KEY is None:
    raise ValueError("SECRET_KEY is not set in the .env file")
