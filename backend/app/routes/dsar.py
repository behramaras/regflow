from uuid import uuid4
from fastapi import APIRouter
from app.services.audit import log_event
from app.schemas.dsar import DSARRequestCreate
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.dsar import DSARRequest

router = APIRouter(
    prefix="/dsar",
    tags=["DSAR"]
)

@router.post("/request")
def create_dsar_request(
    request: DSARRequestCreate,
    db: Session = Depends(get_db)
):
    request_id = str(uuid4())

    dsar_request = DSARRequest(
        id=request_id,
        email=request.email,
        request_type=request.request_type,
        status="pending_verification"
    )

    db.add(dsar_request)
    db.commit()

    log_event(
        event="DSAR_REQUEST_CREATED",
        request_id=request_id
    )

    return {
        "request_id": request_id,
        "message": "DSAR request submitted",
        "status": "pending_verification"
    }