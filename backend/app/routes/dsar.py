from uuid import uuid4

from fastapi import APIRouter

from app.schemas.dsar import DSARRequestCreate

router = APIRouter(
    prefix="/dsar",
    tags=["DSAR"]
)

@router.post("/request")
def create_dsar_request(request: DSARRequestCreate):

    request_id = str(uuid4())

    return {
        "request_id": request_id,
        "message": "DSAR request submitted",
        "status": "pending_verification"
    }