#!/usr/bin/python3
from base_model import Base
from sqlalchemy import Column, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
import uuid
import datetime


class TimeEntry(Base):
    """
    defines table for time entries
    """
    __tablename__ = "time_entries"

    id = Column(String, primary_key=True, default=uuid.uuid4())
    task_id = Column(String, ForeignKey("tasks.id"))
    created_at = Column(String, nullable=False, default=(datetime.datetime.now()).isoformat())
    tracked_time = Column(JSON, nullable=False)

    task = relationship("Task", back_populates="time_entries")
