import os
import shutil
import uuid

from fastapi import (
    APIRouter,
    File,
    HTTPException,
    UploadFile,
)

from core.config import UPLOAD_DIR
from exceptions import TranscriptionException
from services.whisper_service import WhisperService

router = APIRouter()

whisper_service = WhisperService()


@router.get("/")
def health():

    return {
        "status": "healthy",
        "service": "Whisper Service",
    }


@router.post("/transcribe")
def transcribe(
    file: UploadFile = File(...),
):

    file_extension = os.path.splitext(file.filename)[1]

    file_name = f"{uuid.uuid4()}{file_extension}"

    file_path = os.path.join(
        UPLOAD_DIR,
        file_name,
    )

    try:

        os.makedirs(
            UPLOAD_DIR,
            exist_ok=True,
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer,
            )

        return whisper_service.transcribe(file_path)

    except TranscriptionException as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

    finally:

        if os.path.exists(file_path):
            os.remove(file_path)