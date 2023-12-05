import sqlalchemy as sa
from models.CustomerTicket import CustomerTicket
from models.MenuItem import MenuItem
from sqlalchemyconfig import db

customer_ticket_to_menu_m2m = db.Table(
    "customer_ticket_to_menu",
    sa.Column("customer_ticket_id", sa.ForeignKey(CustomerTicket.id), primary_key=True),
    sa.Column("menu_item_id", sa.ForeignKey(MenuItem.id), primary_key=True),
)