#!/usr/bin/python3
from dependencies.get_db import get_db
from dependencies.update_target import update_target
from dependencies.time_entry_deps import add_time_entry
from models.task_model import Task
from models.target_model import Target
from models.user_model import User
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import and_
import uuid
import datetime


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

    update_target(started_at, user)

    response = {
        "task": new_task.to_dict()
    }

    return jsonify(response), 201

    
@task.route("/start", methods=["PATCH"])
@jwt_required()
def start_task():
    """
    start tracking a task
    """
    db = next(get_db())
    user = get_jwt_identity()

    task_id = request.json.get("id", None)
    task_started_at = request.json.get("started_at", datetime.datetime.now().isoformat())

    return_task_id = ""

    if task_id is not None:
        task = db.query(Task).get(task_id)
        task.started_at = task_started_at
        task.is_stopped = False
        task.user_id = user

        db.commit()
        db.refresh(task)

        return_task_id = task_id
    
    if task_id is None:
        new_task_id = uuid.uuid4()
        task_title = request.json.get("title", "")
        task_description = request.json.get("description", "")

        task = Task()
        task.id = new_task_id
        task.title = task_title
        task.description = task_description
        task.started_at = task_started_at
        task.is_stopped = False
        task.user_id = user

        db.add(task)
        db.commit()
        db.refresh(task)

        return_task_id = new_task_id

        started_at = task.to_dict()["started_at"][0:10]

        update_target(started_at, user)


    response = {
        "id": return_task_id,
        "started_at": task.started_at
    }

    return jsonify(response), 201


@task.route("/stop", methods=["PATCH"])
@jwt_required()
def stop_task():
    """
    stop tracking a task
    """
    task_id = request.json.get("id")
    stopped_at = request.json.get("stopped_at")

    db = next(get_db())

    task = db.query(Task).filter(Task.id==task_id).one_or_none()
    if task is None:
        return jsonify({
            "msg": "task id doesn't exist"
        }), 400
    
    if task.is_stopped == False:
        task.stopped_at = stopped_at
        task.is_stopped = True
        
        db.add(task)
        db.commit()
        db.refresh(task)

        add_time_entry(task.started_at, stopped_at, task_id)
    
    response = {
        "stopped_at": task.stopped_at
    }

    return jsonify(response), 201


@task.route("/", methods=["PATCH"])
@jwt_required()
def edit_task():
    """
    edit task details:
    title
    description
    is_major
    """
    db = next(get_db())

    task_id = request.json.get("id")
    task_edit_cols = request.json.get("task_edit")

    task = db.query(Task).get(task_id)
    if task is None:
        return jsonify({
            "msg": "task doesn't exist"
        })
    
    for key, value in task_edit_cols.items():
        if key == "id" or key == "user_id":
            pass
        else:
            setattr(task, key, value)
    
    db.commit()
    db.refresh(task)

    response = task.to_dict()

    return jsonify(response), 200


@task.route("/", methods=["GET"])
@jwt_required()
def get_tasks():
    """
    get a user's daily tasks
    """
    db = next(get_db())
    user = get_jwt_identity()
    date = datetime.datetime.now().isoformat()[0:10]

    tasks = [
        task.to_dict() 
        for task 
        in db.query(Task).filter(and_(Task.user_id==user, Task.started_at.contains(date)), Task.is_deleted==False).all()
    ]

    return jsonify(tasks), 200
