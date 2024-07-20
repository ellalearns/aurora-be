#!/usr/bin/python3
from .base_model import Base
from sqlalchemy import Column, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
import uuid
import datetime


class TimeEntry(Base):
    """
    defines table for time entries
    """
    __tablename__ = "time_entries"

    id = Column(String(512), primary_key=True, default=lambda: uuid.uuid4())
    task_id = Column(String(512), ForeignKey("tasks.id"))
    tracked_time = Column(JSON, nullable=False)

    created_at = Column(String(512),default=lambda: (datetime.datetime.now()).isoformat())
    updated_at = Column(String(512), default=lambda: datetime.datetime.now().isoformat())

    task = relationship("Task", back_populates="time_entries")

    def to_dict(self):
        """
        """
        return {
            "id": self.id,
            "task_id": self.task_id,
            "created_at": self.created_at,
            "tracked_time": self.tracked_time
        }
