from flask import jsonify, request
from flaskapp import app

from models.CustomerTicket import CustomerTicket
from models.MenuItem import MenuItem
from models.TicketToMenu import customer_ticket_to_menu_m2m

# CRUD routes for specific objects in routes folder/module
import routes.waiterRoutes
import routes.menuitems
import routes.ticket

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Table total route
@app.route("/ticket/total", methods=['POST'])
def ticket_total():
    content = request.get_json()

    ticket = CustomerTicket.query.filter(CustomerTicket.table_id == content["table_id"]).first()
    
    total = 0
    item:MenuItem
    for item in ticket.items:
        total += item.price

    return jsonify({"total": float(total)})

@app.route("/total-revenue")
def get_total_revenue():
    item: MenuItem
    tickets: list[CustomerTicket]

    tickets = CustomerTicket.query.all()
    total = 0
    for ticket in tickets:
        for item in ticket.items:
            total += item.price
    return jsonify({"total":float(total)})