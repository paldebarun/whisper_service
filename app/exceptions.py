class WhisperException(Exception):
    pass


class InvalidAudioException(WhisperException):
    pass


class TranscriptionException(WhisperException):
    pass