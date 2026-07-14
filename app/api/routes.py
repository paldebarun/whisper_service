from fastapi import APIRouter

from models.job_model import WhisperJob
from services.job_service import JobService


router = APIRouter()

job_service = JobService()


@router.get("/")
def health():

    return {
        "status": "healthy",
        "service": "Whisper Service",
    }


@router.post("/jobs")
def submit_job(
    request: WhisperJob,
):

    job_service.submit(
        request,
    )

    return {
        "task_id": request.task_id,
        "status": "QUEUED",
    }