#!/usr/bin/python3
from models.target_model import Target
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request
from dependencies.get_db import get_db
import datetime
from sqlalchemy import and_

target = Blueprint("target", __name__)

@target.route("/")
@jwt_required()
def get_progress():
    """
    get total tasks plus done
    """
    db = next(get_db())
    user = get_jwt_identity()
    date = datetime.datetime.now().isoformat()

    target = db.query(Target).filter(and_(
        Target.user_id==user,
        Target.date.contains(date[0:10])
    )).one_or_none()

    if target is None:
        response = {
        "tasks_total": 0,
        "tasks_done": 0
        }
    else:
        target_dict = target.to_dict()
        response = {
        "tasks_total": target_dict["tasks_total"],
        "tasks_done": target_dict["tasks_done"]
        }

    return jsonify(response), 200

