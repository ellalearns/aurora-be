#!/usr/bin/python3
from dependencies.get_db import get_db
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from flask_jwt_extended import set_access_cookies, unset_access_cookies
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
    response = jsonify({"msg": "done"})
    set_access_cookies(response, token)
    return response


@auth.route("/sign-up", methods=["POST"])
def sign_up():
    """
    creates a new user
    returns access token
    """
    new_user_email = request.json.get("email")
    if new_user_email is None\
        or new_user_email == ""\
            or "@" not in new_user_email:
         return jsonify({"msg": "incorrect email"}), 400
    
    new_user_password = request.json.get("password")
    if new_user_password is None or new_user_password == "":
        return jsonify({"msg": "invalid password"}), 400
    
    new_user_username = request.json.get("username")
    if new_user_username is None or new_user_username == "":
        return jsonify({"msg": "invalid username"})
    
    new_user = User(
        email=new_user_email,
        password=new_user_password,
        username=new_user_username
    )

    db = next(get_db())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token = create_access_token(identity=new_user.id)
    
    return jsonify({
        "new_user_id": new_user.id,
        "new_user_username": new_user.username,
        "token": access_token
    }), 201


@auth.route("/sign-out")
@jwt_required()
def sign_out():
    """
    """
    response = jsonify({"msg": "see ya later!"})
    unset_access_cookies(response=response)
    return response
