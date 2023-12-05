import sqlalchemy as sa
from models.CustomerTicket import CustomerTicket
from models.Menu import Menu
from sqlalchemyconfig import db

customer_ticket_to_menu_m2m = db.Table(
    "customer_ticket_to_menu",
    sa.Column("customer_ticket_id", sa.ForeignKey(CustomerTicket.id), primary_key=True),
    sa.Column("menu_id", sa.ForeignKey(Menu.id), primary_key=True),
)