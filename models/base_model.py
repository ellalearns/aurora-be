#!/usr/bin/python3
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#get values from env files
load_dotenv()
DB = os.getenv("DB")
DIALECT = os.getenv("DIALECT")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
DB_NAME = os.getenv("DB_NAME")

#create sql engine
engine = create_engine(
    f"{DB}+{DIALECT}://{USER}:{PASSWORD}@{HOST}/{DB_NAME}",
    echo=True,
    pool_pre_ping=True
    )

#create connection session
Session = sessionmaker()
Session.configure(bind=engine)
db = Session()

#create base model
Base = declarative_base()
