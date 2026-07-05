from pathlib import Path

from faster_whisper import WhisperModel

from core.config import (
    COMPUTE_TYPE,
    DEVICE,
    WHISPER_MODEL,
)
from exceptions import TranscriptionException
from models.response_models import (
    TranscriptResponse,
    TranscriptSegment,
)


class WhisperService:

    def __init__(self):

        self.model = WhisperModel(
            WHISPER_MODEL,
            device=DEVICE,
            compute_type=COMPUTE_TYPE,
        )

    def transcribe(self, audio_path: str) -> TranscriptResponse:

        try:

            print("Loading audio:", audio_path)

            segments, info = self.model.transcribe(audio_path)

            print("Whisper started decoding")

            transcript_segments = []
            transcript_text = []

            for segment in segments:

                print(segment.text)

                transcript_segments.append(
                    TranscriptSegment(
                        start=segment.start,
                        end=segment.end,
                        text=segment.text.strip(),
                    )
                )

                transcript_text.append(segment.text.strip())

            print("Finished transcription")

            return TranscriptResponse(
                language=info.language,
                duration=info.duration,
                text=" ".join(transcript_text),
                segments=transcript_segments,
            )

        except Exception as e:
            print(e)
            raise TranscriptionException(
                "Failed to transcribe audio."
            ) from e