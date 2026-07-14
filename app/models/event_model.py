from datetime import UTC, datetime

from pydantic import BaseModel, Field

from models.response_models import WhisperResponse


class WhisperCompletedEvent(BaseModel):

    task_id: str

    event_type: str = "whisper.completed"

    payload: WhisperResponse

    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )


class WhisperFailedEvent(BaseModel):

    task_id: str

    event_type: str = "whisper.failed"

    error: str

    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )