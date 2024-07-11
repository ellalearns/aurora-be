#!/usr/bin/python3
from .base_model import Base
import datetime
from sqlalchemy import Column, String, Integer, Text, Boolean, JSON, ForeignKey
from sqlalchemy.orm import relationship
import uuid


class Task(Base):
    """
    defines the tasks table
    """
    __tablename__ = "tasks"

    id = Column(String(512), primary_key=True, default=uuid.uuid4())
    title = Column(String(512), nullable=False, default="")
    description = Column(Text, nullable=True)
    started_at = Column(String(512), nullable=False, default=(datetime.datetime.now()).isoformat())
    stopped_at = Column(String(512), nullable=True)
    completed = Column(Boolean, nullable=False, default=False)
    tags = Column(JSON, nullable=True)
    major = Column(Integer, nullable=False, default=0)
    recurring = Column(Boolean, default=False)
    recurring_timeblock = Column(String(512), nullable=True)
    deleted = Column(Boolean, default=False)
    user_id = Column(String(512), ForeignKey("users.id"))

    user = relationship("User", back_populates="tasks")
    time_entries = relationship("TimeEntry", back_populates="task", cascade="all, delete, delete-orphan")

    def to_dict(self):
        """
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "started_at": self.started_at,
            "stopped_at": self.stopped_at,
            "completed": self.completed,
            "tags": self.tags,
            "major": self.major,
            "recurring": self.recurring,
            "recurring_timeblock": self.recurring_timeblock,
            "deleted": self.deleted,
            "user_id": self.user_id,
            "time_entries": [time_entry.to_dict() for time_entry in self.time_entries]
        }
