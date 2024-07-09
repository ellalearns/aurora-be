#!/usr/bin/python3
from base_model import Base
from sqlalchemy import Column, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
import uuid


class Report(Base):
    """
    defines table for user reports
    """
    __tablename__ = "reports"

    id = Column(String, primary_key=True, default=uuid.uuid4())
    user_id = Column(String, ForeignKey("users.id"))
    daily_time = Column(JSON, nullable=True)

    user = relationship("User", back_populates="reports")