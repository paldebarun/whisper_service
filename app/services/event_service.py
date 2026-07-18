from app.messaging.redis_stream import RedisStream

from app.core.config import EVENT_STREAM

from app.models.event_model import (
    WhisperCompletedEvent,
    WhisperFailedEvent,
)


class EventService:

    def __init__(self):

        self.stream = RedisStream()

    def publish_completed(
        self,
        event: WhisperCompletedEvent,
    ):

        self.stream.publish(
            EVENT_STREAM,
            event.model_dump(mode="json"),
        )

    def publish_failed(
        self,
        task_id: str,
        error: str,
    ):

        event = WhisperFailedEvent(
            task_id=task_id,
            error=error,
        )

        self.stream.publish(
            EVENT_STREAM,
            event.model_dump(mode="json"),
        )