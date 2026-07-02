from pydantic import BaseModel


class TranscriptSegment(BaseModel):

    start: float

    end: float

    text: str


class TranscriptResponse(BaseModel):

    language: str

    duration: float

    text: str

    segments: list[TranscriptSegment]