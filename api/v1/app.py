#!/usr/bin/python3
import os
from datetime import timedelta
from dependencies.get_db import get_db
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import jwt_required, JWTManager
from models.user_model import User
from routes.auth_route import auth




app = Flask(__name__)
app.register_blueprint(auth, url_prefix="/auth")


CORS(app, resources={
    r"/*": {
        "origins": "http://localhost:3000"
    }
})


load_dotenv()
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=3)
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
jwt = JWTManager(app)


@app.route("/")
def hello_world():
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
    all_users_list = [user.to_dict() for user in all_users]
    return all_users_list




if __name__ == "__main__":
    app.run(debug=True)
