from pydantic import BaseModel, EmailStr


class DSARRequestCreate(BaseModel):
    email: EmailStr
    request_type: str


class DSARRequestResponse(BaseModel):
    request_id: str
    status: str
    message: str

class DSARStatusUpdate(BaseModel):
    status: str
    