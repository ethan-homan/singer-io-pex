import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SERVICE_PORT = int(os.getenv("PORT"))
SERVICE_HOST = "0.0.0.0"
PEX_SINGER_BASE_PATH = "dist"

__all__ = [
    SERVICE_PORT,
    SERVICE_HOST,
]
