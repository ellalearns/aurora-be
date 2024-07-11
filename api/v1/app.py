#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_cors import CORS
from dependencies.get_db import get_db
from models.user_model import User
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, JWTManager
import os
from dotenv import load_dotenv


app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": "http://localhost:3000"
    }
})

load_dotenv()
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)

@app.route("/")
def hello_world():
    """
    """
    return "<p>first steps</>"

@app.route("/welcome")
def welcome_user():
    """
    """
    return {
        "greeting": "welcome, sailor :)"
    }

@app.route("/testdb")
@jwt_required()
def test_db():
    """
    """
    db = next(get_db())
    all_users = db.query(User).all()
    return jsonify(all_users), 200

@app.route("/get-token", methods=["POST"])
def get_token():
    """
    """
    username = request.json.get("username")
    if username != "test":
        return jsonify({"msg": "incorrect username"}), 401
    
    token = create_access_token(identity=username)
    return jsonify(token=token), 201

if __name__ == "__main__":
    app.run(debug=True)
