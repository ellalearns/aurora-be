#!/usr/bin/python3
from base_model import Base
from sqlalchemy import Column, Integer, String
import uuid
import datetime


class User(Base):
    """
    defines the User table
    """
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=uuid.uuid4())
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(String, default=(datetime.datetime.now()).isoformat())
    updated_at = Column(String, default=(datetime.datetime.now()).isoformat())
