#!/usr/bin/python3
from dependencies.get_db import get_db
from models.task_model import Task
from models.target_model import Target
from models.user_model import User
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import and_


task = Blueprint("task", __name__)


@task.route("/", methods=["POST"])
@jwt_required()
def create_task():
    """
    handles creating a new task
    """
    user = get_jwt_identity()

    if request.json.get("title", None) == None:
        return jsonify({
            "msg": "pls add a title for task"
        }), 400

    request_dict = request.json
    request_dict["user_id"] = user

    new_task = Task()
    for key, value in request_dict.items():
        setattr(new_task, key, value)
    
    db = next(get_db())
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    started_at = new_task.to_dict()["started_at"][0:10]
    target = db.query(Target).filter(and_(Target.user_id==user, Target.date.contains(started_at))).one_or_none()
    if target is None:
        target = Target(
            user_id=user,
            daily_target=db.query(User).filter(User.id==user).one().daily_target,
            tasks_total=1
        )
    else:
        target.tasks_total = target.tasks_total + 1

    
    db.add(target)
    db.commit()
    db.refresh(target)

    response = {
        "id": new_task.id,
    }

    return jsonify(response), 201

    



