from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()


def resolve_path(env_name: str, default: str) -> Path:
    """
    Resolve a directory path from an environment variable.

    Relative paths are resolved relative to the project directory.
    Absolute paths are used directly.
    """

    base_dir = Path(__file__).resolve().parent.parent

    path = Path(os.getenv(env_name, default))

    if not path.is_absolute():
        path = base_dir / path

    path.mkdir(
        parents=True,
        exist_ok=True,
    )

    return path


WHISPER_MODEL = os.getenv(
    "WHISPER_MODEL",
    "small",
)

DEVICE = os.getenv(
    "DEVICE",
    "cpu",
)

COMPUTE_TYPE = os.getenv(
    "COMPUTE_TYPE",
    "int8",
)

UPLOAD_DIR = resolve_path(
    "UPLOAD_DIR",
    "uploads",
)