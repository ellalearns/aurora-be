#!/usr/bin/python3
from dependencies.get_db import get_db
from models.user_model import User
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity


user = Blueprint("user", __name__)
db = next(get_db())


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
        return jsonify({"msg": "incorrect tokens"}), 400
    
    user = db.query(User).filter(User.id==user_id).one()

    return jsonify({
        "user": user.to_dict()
    }), 200
