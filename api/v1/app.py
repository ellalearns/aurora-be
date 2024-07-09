#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)


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
