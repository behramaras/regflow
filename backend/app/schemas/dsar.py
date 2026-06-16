from pydantic import BaseModel, EmailStr


class DSARRequestCreate(BaseModel):
    email: EmailStr
    request_type: str