#!/usr/bin/python3
from .base_model import Base
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
import uuid
import datetime


class User(Base):
    """
    defines the User table
    """
    __tablename__ = "users"

    id = Column(String(512), primary_key=True, default=lambda: uuid.uuid4())
    username = Column(String(512), nullable=False)
    email = Column(String(512), nullable=False, unique=True)
    password = Column(String(512), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(String(512), default=(datetime.datetime.now()).isoformat())
    updated_at = Column(String(512), default=(datetime.datetime.now()).isoformat())

    tasks = relationship("Task", back_populates="user", cascade="all, delete, delete-orphan")
    reports = relationship("Report", back_populates="user", cascade="all, delete, delete-orphan")

    def check(self):
        """
        returns dictionary instance of user
        """
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "is_deleted": self.is_deleted,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    def to_dict(self):
        """
        user details safe to return in json objects
        """
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "tasks": [task.to_dict() for task in self.tasks],
            "reports": [report.to_dict() for report in self.reports]
        }
