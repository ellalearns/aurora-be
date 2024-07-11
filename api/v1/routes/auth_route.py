#!/usr/bin/python3
from dependencies.get_db import get_db
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from models.user_model import User

auth = Blueprint("auth", __name__)

@auth.route("/sign-in", methods=["POST"])
def sign_in():
    """
    signs in a user
    returns an access token
    """
    email = request.json.get("email")
    password = request.json.get("password")
    
    db = next(get_db())

    try:
        user = db.query(User).filter(User.email==email).one().to_dict()
    except:
        return jsonify({"msg": "improper request"}), 400
    
    if user is None or user["password"] != password:
        return jsonify({"msg": "incorrect details"}), 401
    
    token = create_access_token(identity=user["id"])
    return jsonify({"msg": "logged in :)", "token": token}), 200

