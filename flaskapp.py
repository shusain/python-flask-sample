'''
Creates a Flask App and configures the app for [Flask-SqlAlchemy library](https://flask-sqlalchemy.palletsprojects.com/)
'''
from flask import Flask
from sqlalchemyconfig import db

app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///restaurant.sqlite"
# initialize the app with the extension
db.init_app(app)