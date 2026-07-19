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



PORT = int(
    os.getenv(
        "PORT",
        "8000",
    )
)

WHISPER_QUEUE = "whisper_queue"

EVENT_STREAM = "workflow_events"

EVENT_CONSUMER_GROUP = "workflow_group"

EVENT_CONSUMER_NAME = "whisper_service"

REDIS_HOST = os.getenv(
    "REDIS_HOST",
    "localhost",
)

REDIS_PORT = int(
    os.getenv(
        "REDIS_PORT",
        "6379",
    )
)

REDIS_PASSWORD = os.getenv(
    "REDIS_PASSWORD",
)

REDIS_DB = int(
    os.getenv(
        "REDIS_DB",
        "0",
    )
)