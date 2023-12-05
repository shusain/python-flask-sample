from flask import jsonify, request
from flaskapp import app
from models.CustomerTicket import CustomerTicket
from sqlalchemyconfig import db

# Customer Ticket Routes
@app.route("/ticket", methods=["GET"])
def ticket_list():
    tickets = CustomerTicket.query.all()
    return jsonify(tickets)

@app.route("/ticket", methods=["POST"])
def ticket_create():
    content = request.get_json()

    ticket = CustomerTicket(
        arrival=content["arrival"],
        departed=content["departed"],
        table_id=content["table_id"],
        waiter_id=content["waiter_id"]
    )

    db.session.add(ticket)
    db.session.commit()

    return jsonify({ "success": True })