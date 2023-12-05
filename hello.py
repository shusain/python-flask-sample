from flask import Flask, jsonify, request
from sqlalchemyconfig import db

from models.CustomerTicket import CustomerTicket
from models.Menu import Menu
from models.Waiter import Waiter
from models.TicketToMenu import customer_ticket_to_menu_m2m


app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///restaurant.sqlite"
# initialize the app with the extension
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Waiter Routes
@app.route("/waiter", methods=["GET"])
def waiter_list():
    waiters = db.session.execute(db.select(Waiter)).scalars()
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


# Menu Item Routes
@app.route("/menu", methods=["GET"])
def menu_item_list():
    menu_items = Menu.query.all()
    return jsonify(menu_items)

@app.route("/menu", methods=["POST"])
def menu_item_create():
    content = request.get_json()

    menu_item = Menu(
        item_name=content["item_name"],
        description=content["description"],
        price=content["price"]
    )

    db.session.add(menu_item)
    db.session.commit()

    return jsonify({ "success": True })


# Customer Ticket Routes
@app.route("/ticket", methods=["GET"])
def ticket_list():
    tickets = db.session.execute(db.select(CustomerTicket)).scalars()
    return jsonify(tickets)

@app.route("/ticket", methods=["POST"])
def ticket_create():
    content = request.get_json()

    ticket = CustomerTicket(
        arrival=content["arrival"],
        departed=content["departed"],
        table_id=content["table_id"]
    )

    db.session.add(ticket)
    db.session.commit()

    return jsonify({ "success": True })

# Table total route
@app.route("/ticket/total", methods=['POST'])
def ticket_total():
    content = request.get_json()

    ticket = CustomerTicket.query.filter(CustomerTicket.table_id == content["table_id"]).first()
    
    total = 0
    item:Menu
    for item in ticket.items:
        total += item.price

    return jsonify({"total": float(total)})

@app.route("/total-revenue")
def get_total_revenue():
    item: Menu
    tickets: list[CustomerTicket]

    tickets = CustomerTicket.query.all()
    total = 0
    for ticket in tickets:
        for item in ticket.items:
            total += item.price
    return jsonify({"total":float(total)})