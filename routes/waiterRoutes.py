from flask import jsonify, request
from flaskapp import app
from sqlalchemyconfig import db
from models.Waiter import Waiter

# Waiter Routes
@app.route("/waiter", methods=["GET"])
def waiter_list():
    waiters = Waiter.query.all()
    return jsonify(waiters)

@app.route("/waiter", methods=["POST"])
def waiter_create():
    content = request.get_json()
    waiter = Waiter(
        first_name=content["first_name"],
        last_name=content["last_name"],
        tax_number=content["tax_number"]
    )
    db.session.add(waiter)
    db.session.commit()

    return jsonify({ "success": True })