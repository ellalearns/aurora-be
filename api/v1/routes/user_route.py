#!/usr/bin/python3
from dependencies.get_db import get_db
from models.user_model import User
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity, unset_access_cookies


user = Blueprint("user", __name__)


@user.route("/")
@jwt_required()
def get_user():
    """
    get a user's details
    """
    user_id = ""
    try:
        user_id = get_jwt_identity()
    except:
        return jsonify({"msg": "incorrect tokens"}), 401
    
    db = next(get_db())
    user = db.query(User).filter(User.id==user_id).one()

    return jsonify({
        "user": user.to_dict()
    }), 200


@user.route("/edit-username", methods=["PATCH"])
@jwt_required()
def edit_username():
    """
    edit a user's username
    """
    new_username = request.json.get("new_username")
    if new_username is None or new_username == "":
        return jsonify({
            "msg": "invalid username"
        }), 400
    
    user_id = ""
    try:
        user_id = get_jwt_identity()
    except:
        return 401
    
    db = next(get_db())

    user = db.query(User).filter(User.id==user_id).one()
    user.username = new_username
    db.commit()
    db.refresh(user)

    return jsonify({
        "new_username": user.to_dict()["username"]
    }), 201


@user.route("/delete-user", methods=["DELETE"])
@jwt_required()
def delete_user():
    """
    soft deletes a user
    """
    user_id = ""
    try:
        user_id = get_jwt_identity()
    except:
        return 401
    
    db = next(get_db())
    
    user = db.query(User).filter(User.id==user_id).one()
    user.email = "del_" + user.email
    user.is_deleted = True
    db.commit()
    db.refresh(user)

    response = jsonify({
        "msg": "sad to see you go"
    })

    unset_access_cookies(response=response)

    return response
