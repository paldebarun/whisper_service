from pathlib import Path

from faster_whisper import WhisperModel

from app.core.config import (
    COMPUTE_TYPE,
    DEVICE,
    WHISPER_MODEL,
)

from app.exceptions import TranscriptionException

from app.models.response_models import (
    WhisperResponse,
    TranscriptSegment,
)

from app.utils.logger import Logger

logger = Logger.get_logger()


class WhisperService:

    def __init__(self):

        self.model = WhisperModel(
            WHISPER_MODEL,
            device=DEVICE,
            compute_type=COMPUTE_TYPE,
        )

    def transcribe(
        self,
        audio_path: str,
    ) -> WhisperResponse:

        audio_file = Path(audio_path)

        if not audio_file.exists():

            raise TranscriptionException(
                f"Audio file not found: {audio_path}"
            )

        try:

            logger.info(
                f"Transcribing audio: {audio_path}"
            )

            segments, info = self.model.transcribe(
                str(audio_file),
            )

            transcript_segments = []

            transcript_text = []

            for segment in segments:

                transcript_segments.append(
                    TranscriptSegment(
                        start=segment.start,
                        end=segment.end,
                        text=segment.text.strip(),
                    )
                )

                transcript_text.append(
                    segment.text.strip()
                )

            logger.info(
                "Transcription completed successfully."
            )

            return WhisperResponse(
                language=info.language,
                duration=info.duration,
                text=" ".join(transcript_text),
                segments=transcript_segments,
            )

        except Exception as e:

            logger.error(
                f"Transcription failed: {e}"
            )

            raise TranscriptionException(
                "Failed to transcribe audio."
            ) from e