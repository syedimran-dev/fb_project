from flask import Flask
from flask_restx import Api
from models import db, User, Post, React, Comment
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate
import os
from auth import auth_ns
from post import post_ns
from react import react_ns
from comment import comment_ns

app = Flask(__name__)
api = Api(app, doc='/docs')
api.add_namespace(auth_ns)
api.add_namespace(post_ns)
api.add_namespace(react_ns)
api.add_namespace(comment_ns)

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
SECRET_KEY = 'SECRET_KEY'
SQLALCHEMY_TRACK_MODIFICATIONS = 'SQLALCHEMY_TRACK_MODIFICATIONS'
app.config[ 'SQLALCHEMY_DATABASE_URI' ]= "sqlite:///"+os.path.join(BASE_DIR, 'facebook.db')
app.config["JWT_SECRET_KEY"] = "super-secret"
db.init_app(app)

# Migrate
Migrate(app, db)

# Cors
CORS(app)

# jwt

JWTManager(app)


with app.app_context():
    db.create_all()

@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Post": Post,
        "user": User,
        "react": React,
        "comment": Comment
    }

if __name__ == "__main__":
    app.run(debug=True)