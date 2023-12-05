# Importing flask app and DB for shared DB/App configuration

from flaskapp import app
from sqlalchemyconfig import db

# Importing all the models so when we run this standalone it has reference to them
# to generate tables in the DB.

from models.CustomerTicket import CustomerTicket
from models.MenuItem import MenuItem
from models.Waiter import Waiter
from models.TicketToMenu import customer_ticket_to_menu_m2m


# Creating an app context and running all the table creation based on ORM-models in the DB
with app.app_context():
    db.create_all()