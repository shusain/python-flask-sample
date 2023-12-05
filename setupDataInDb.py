
from flask import Flask
from models.CustomerTicket import CustomerTicket
from models.Menu import Menu
from models.Waiter import Waiter
from models.TicketToMenu import customer_ticket_to_menu_m2m
from sqlalchemyconfig import db

app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///restaurant.sqlite"
# initialize the app with the extension
db.init_app(app)

with app.app_context():
    db.create_all()

    bob = Waiter(first_name="Bob", last_name="Smith", tax_number="1234")
    joe = Waiter(first_name="Joe", last_name="Thomas", tax_number="5432")


    hotdog = Menu(item_name="hotdog", description="a tasty dog", price=2.99)
    burger = Menu(item_name="burger", description="a scrumptous burger", price=9.99)

    customer1_ticket = CustomerTicket(arrival="2:00", departed="2:25", table_id=10)
    customer2_ticket = CustomerTicket(arrival="1:00", departed="6:25", table_id=40)

    customer1_ticket.items = [hotdog, burger]
    customer1_ticket.waiter = joe

    customer2_ticket.items = [burger]
    customer2_ticket.waiter = bob

    db.session.add_all([customer1_ticket, customer2_ticket])
    db.session.commit()