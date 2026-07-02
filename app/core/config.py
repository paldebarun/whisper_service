import os

from dotenv import load_dotenv

load_dotenv()

WHISPER_MODEL = os.getenv(
    "WHISPER_MODEL",
    "small"
)

DEVICE = os.getenv(
    "DEVICE",
    "cpu"
)

COMPUTE_TYPE = os.getenv(
    "COMPUTE_TYPE",
    "int8"
)

UPLOAD_DIR = os.getenv(
    "UPLOAD_DIR",
    "uploads"
)