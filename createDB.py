from flaskapp import app
from sqlalchemyconfig import db

with app.app_context():
    db.create_all()