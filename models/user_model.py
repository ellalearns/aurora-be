#!/usr/bin/python3
from .base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import uuid
import datetime


class User(Base):
    """
    defines the User table
    """
    __tablename__ = "users"

    id = Column(String(512), primary_key=True, default=uuid.uuid4())
    username = Column(String(512), nullable=False)
    email = Column(String(512), nullable=False)
    password = Column(String(512), nullable=False)
    created_at = Column(String(512), default=(datetime.datetime.now()).isoformat())
    updated_at = Column(String(512), default=(datetime.datetime.now()).isoformat())

    tasks = relationship("Task", back_populates="user", cascade="all, delete, delete-orphan")
    reports = relationship("Report", back_populates="user", cascade="all, delete, delete-orphan")

    def to_dict(self):
        """
        returns dictionary instance of user
        """
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "tasks": [task.to_dict() for task in self.tasks],
            "reports": [report.to_dict() for report in self.reports]
        }
