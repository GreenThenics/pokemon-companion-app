import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
POKEAPI_BASE = "https://pokeapi.co/api/v2/pokemon"
