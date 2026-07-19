from pydantic import BaseModel


class WhisperJob(BaseModel):

    task_id: str

    audio_path: str