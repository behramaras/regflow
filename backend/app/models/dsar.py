from sqlalchemy import Column, String

from app.db.database import Base


class DSARRequest(Base):
    __tablename__ = "dsar_requests"

    id = Column(String, primary_key=True, index=True)
    email = Column(String, nullable=False)
    request_type = Column(String, nullable=False)
    status = Column(String, nullable=False)