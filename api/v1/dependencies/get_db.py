#!/usr/bin/python3
from db_setup import Session


def get_db():
    """
    get a db connection
    """
    db = Session()
    try:
        yield db
    finally:
        db.close()
