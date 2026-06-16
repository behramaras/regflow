from fastapi import APIRouter

from app.schemas.dsar import DSARRequestCreate

router = APIRouter(
    prefix="/dsar",
    tags=["DSAR"]
)


@router.post("/request")
def create_dsar_request(request: DSARRequestCreate):
    return {
        "message": "DSAR request submitted",
        "email": request.email,
        "request_type": request.request_type,
        "status": "pending_verification"
    }