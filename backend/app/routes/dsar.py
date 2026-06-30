from uuid import uuid4
from fastapi import APIRouter, Depends, HTTPException
from app.services.audit import log_event
from app.schemas.dsar import DSARRequestCreate
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.dsar import DSARRequest
from app.schemas.dsar import DSARStatusUpdate

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

@router.get("/{request_id}")
def get_dsar_request(
    request_id: str,
    db: Session = Depends(get_db)
):

    dsar_request = (
        db.query(DSARRequest)
        .filter(DSARRequest.id == request_id)
        .first()
    )

    if not dsar_request:
        raise HTTPException(
            status_code=404,
            detail="DSAR request not found"
        )

    return {
        "request_id": dsar_request.id,
        "email": dsar_request.email,
        "request_type": dsar_request.request_type,
        "status": dsar_request.status
    }

@router.patch("/{request_id}")
def update_dsar_status(
    request_id: str,
    update: DSARStatusUpdate,
    db: Session = Depends(get_db)
):
    dsar = db.query(DSARRequest).filter(
        DSARRequest.id == request_id
    ).first()

    if not dsar:
        raise HTTPException(
            status_code=404,
            detail="DSAR request not found"
        )

    old_status = dsar.status
    dsar.status = update.status

    db.commit()

    log_event(
    event="DSAR_STATUS_UPDATED",
    request_id=request_id,
    metadata={
        "old_status": old_status,
        "new_status": update.status
    }
)

    return {
        "request_id": request_id,
        "old_status": old_status,
        "new_status": update.status
    }