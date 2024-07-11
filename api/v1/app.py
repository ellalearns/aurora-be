#!/usr/bin/python3
from flask import Flask
from flask_cors import CORS
from models.base_model import db


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


if __name__ == "__main__":
    app.run(debug=True)
