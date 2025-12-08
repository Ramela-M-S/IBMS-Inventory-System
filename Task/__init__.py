from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_restful import Resource, Api, marshal_with, fields, abort, reqparse 


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db?check_same_thread=False"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key="SECRET_KEY12345"
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login_page"
from Task import route