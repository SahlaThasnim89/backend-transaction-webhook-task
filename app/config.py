import os
from dotenv import load_dotenv

load_dotenv()  # loads .env

DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")
