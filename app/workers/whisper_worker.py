from models.job_model import WhisperJob

from services.whisper_service import WhisperService
from services.event_service import EventService
from models.event_model import WhisperCompletedEvent

from messaging.redis_queue import RedisQueue

from core.config import WHISPER_QUEUE

from utils.logger import Logger

logger = Logger.get_logger()

class WhisperWorker:

    def __init__(self):

        self.queue = RedisQueue()

        self.whisper_service = WhisperService()

        self.event_service = EventService()

    def start(self):

        logger.info("Whisper Worker Started")

        while True:

            job = self.queue.pop(
                WHISPER_QUEUE,
            )

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