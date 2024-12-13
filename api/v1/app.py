#!/usr/bin/python3
import os
from datetime import datetime, timedelta, timezone
from dependencies.get_db import get_db
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import jwt_required, JWTManager, set_access_cookies
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity
from models.user_model import User
from routes.auth_route import auth
from routes.user_route import user
from routes.task_route import task
from routes.target_route import target



app = Flask(__name__)
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(task, url_prefix="/task")
app.register_blueprint(target, url_prefix="/target")



CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
}, preflightContinue=True, supports_credentials=True)

app.config["CORS_METHODS"] = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
app.config["CORS_HEADERS"] = ["Content-Type", "Authorization", "x-requested-with"]


load_dotenv()
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=3)
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_CSRF_METHODS"] = []
app.config["JWT_COOKIE_CSRF_PROTECT"] = True
app.config["JWT_COOKIE_SAMESITE"] = "None"
app.config["JWT_COOKIE_SECURE"] = True
jwt = JWTManager(app)



@app.after_request
def refresh_almost_expired_jwt(response):
    try:
        jwt_time = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_time = datetime.timestamp(now + timedelta(minutes=30))
        if target_time > jwt_time:
            new_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, new_token)
        return response
    except (RuntimeError, KeyError):
        return response


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
    all_users = db.query(User).filter(User.is_deleted==False).all()
    all_users_list = [user.to_dict() for user in all_users]
    return all_users_list




if __name__ == "__main__":
    app.run(
        ssl_context=("localhost.pem", "localhost-key.pem"),
        debug=True
        )
