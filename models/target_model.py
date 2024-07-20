#!/usr/bin/python3
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base_model import Base
import uuid
import datetime


class Target(Base):
    """
    defines the targets table
    """
    __tablename__ = "targets"

    id = Column(String(512), primary_key=True, default=lambda: uuid.uuid4())
    user_id = Column(String(512), ForeignKey("users.id"))
    daily_target = Column(Integer, nullable=True)
    date = Column(String(512), default=lambda: datetime.datetime.now().isoformat())
    tasks_total = Column(Integer, default=0)
    tasks_done = Column(Integer, default=0)

    created_at = Column(String(512), default=lambda: datetime.datetime.now().isoformat())
    updated_at = Column(String(512), default=lambda: datetime.datetime.now().isoformat())

    user = relationship("User", back_populates="targets")

    def to_dict(self):
        """
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "daily_target": self.daily_target,
            "date": self.date,
            "tasks_total": self.tasks_total,
            "tasks_done": self.tasks_done
        }