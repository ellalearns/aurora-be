#!/usr/bin/python3
from .base_model import Base
from sqlalchemy import Column, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
import uuid
import datetime


class Report(Base):
    """
    defines table for user reports
    """
    __tablename__ = "reports"

    id = Column(String(512), primary_key=True, default=lambda: uuid.uuid4())
    user_id = Column(String(512), ForeignKey("users.id"))
    daily_time = Column(JSON, default={})

    created_at = Column(String(512), default=lambda: (datetime.datetime.now().isoformat()))
    updated_at = Column(String(512), default=lambda: (datetime.datetime.now().isoformat()))

    user = relationship("User", back_populates="reports")

    def to_dict(self):
        """
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "daily_time": self.daily_time
        }
