from fastapi import APIRouter
from app.models.request_models import ContentRequest
from app.services.pipeline_service import generate_full_content
from app.utils.logger import get_logger

router = APIRouter()
logger = get_logger("api")


@router.post("/generate")
def generate(request: ContentRequest):
    try:
        logger.info(
            f"Incoming request | topic={request.topic} | platform={request.platform} | tone={request.tone} | style={request.style}"
        )

        result = generate_full_content(request)

        logger.info("Request processed successfully")

        return {
            "status": "success",
            "data": result
        }

    except Exception as e:
        # Logs full stack trace internally
        logger.exception("Error in /generate endpoint")

        # Safe response for client
        return {
            "status": "error",
            "message": "Internal server error",
            "hint": "Please try again or check logs if issue persists"
        }