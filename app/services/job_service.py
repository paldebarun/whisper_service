from app.messaging.redis_queue import RedisQueue

from app.core.config import WHISPER_QUEUE

from app.models.job_model import WhisperJob


class JobService:

    def __init__(self):

        self.queue = RedisQueue()

    def submit(
        self,
        job: WhisperJob,
    ):

        self.queue.push(
            WHISPER_QUEUE,
            job.model_dump(),
        )