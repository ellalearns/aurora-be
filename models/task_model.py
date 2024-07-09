#!/usr/bin/python3
from base_model import Base
from user_model import User
import datetime
from sqlalchemy import Column, String, Integer, Text, Boolean, JSON, ForeignKey
from sqlalchemy.orm import relationship
import uuid


class Task(Base):
    """
    defines the tasks table
    """
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, default=uuid.uuid4())
    title = Column(String, nullable=False, default="")
    description = Column(Text, nullable=True)
    started_at = Column(String, nullable=False, default=(datetime.datetime.now()).isoformat())
    stopped_at = Column(String, nullable=True)
    completed = Column(Boolean, nullable=False, default=False)
    tags = Column(JSON, nullable=True)
    major = Column(Integer, nullable=False, default=0)
    recurring = Column(Boolean, default=False)
    recurring_timeblock = Column(String, nullable=True)
    deleted = Column(Boolean, default=False)
    user_id = Column(String, ForeignKey("users.id"))

    user = relationship("User", back_populates="tasks")
    time_entries = relationship("TimeEntry", back_populates="task", cascade="all, delete, delete-orphan")
