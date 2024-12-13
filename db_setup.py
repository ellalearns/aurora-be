#!/usr/bin/python3
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.user_model import User
from models.task_model import Task
from models.time_entry_model import TimeEntry
from models.report_model import Report
from models.target_model import Target


#get values from env files
load_dotenv()
DB = os.getenv("DB")
DIALECT = os.getenv("DIALECT")
USER = os.getenv("USER")
PASSWORD = os.getenv("PWD")
HOST = os.getenv("HOST")
DB_NAME = os.getenv("DB_NAME")

#create sql engine
engine = create_engine(
    f"{DB}+{DIALECT}://{USER}:{PASSWORD}@{HOST}/{DB_NAME}",
    echo=True,
    pool_pre_ping=True,
    pool_size=30,
    max_overflow=10
    )

#create connection session
# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
