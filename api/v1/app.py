#!/usr/bin/python3
from flask import Flask, jsonify
from flask_cors import CORS
from dependencies.get_db import get_db
from models.user_model import User


app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": "http://localhost:3000"
    }
})

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
def test_db():
    """
    """
    db = next(get_db())
    all_users = db.query(User).all()
    return jsonify(all_users), 200

if __name__ == "__main__":
    app.run(debug=True)
