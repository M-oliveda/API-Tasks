from os import getenv
from dotenv import load_dotenv

load_dotenv()


class Config:
    PORT = getenv("PORT", 3300)
    HOST = getenv("HOST") or "localhost"
    DEVELOPMENT_MODE = getenv("DEBUG") or False
