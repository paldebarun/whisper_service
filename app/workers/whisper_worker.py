import redis

from app.models.job_model import WhisperJob

from app.services.whisper_service import WhisperService
from app.services.event_service import EventService
from app.models.event_model import WhisperCompletedEvent

from app.messaging.redis_queue import RedisQueue

from app.core.config import WHISPER_QUEUE

from app.utils.logger import Logger

logger = Logger.get_logger()


class WhisperWorker:

    def __init__(self):

        self.queue = RedisQueue()

        self.whisper_service = WhisperService()

        self.event_service = EventService()

    def start(self):

        logger.info("Whisper Worker Started")

        while True:

            try:
                job = self.queue.pop(
                    WHISPER_QUEUE,
                )
            except redis.exceptions.TimeoutError:
                continue

            if job is None:

                continue

            try:

                self.process_job(job)

            except Exception as e:

                task_id = job.get(
                    "task_id",
                    "unknown",
                )

                self.event_service.publish_failed(
                    task_id=task_id,
                    error=str(e),
                )

                logger.error(
                    f"Task {task_id} failed: {e}"
                )

    def process_job(
        self,
        job: dict,
    ):

        whisper_job = WhisperJob(**job)

        result = self.whisper_service.transcribe(
            whisper_job.audio_path,
        )

        event = WhisperCompletedEvent(
            task_id=whisper_job.task_id,
            payload=result,
        )

        self.event_service.publish_completed(
            event
        )

        logger.info(
            f"Completed Whisper: {whisper_job.task_id}"
        )