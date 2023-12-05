
from sqlalchemy import Column, ForeignKey, Integer, String
from models.Waiter import Waiter

from sqlalchemyconfig import db

class CustomerTicket(db.Model):
    id = Column(Integer, primary_key=True)
    arrival = Column(String)
    departed = Column(String)
    table_id = Column(Integer)

    # Customer ticket must be assigned to waiter (only one ticket per waiter)
    waiter = db.relationship(Waiter)
    waiter_id = Column(ForeignKey("waiter.id"))
    
    # Customer ticket must allow for multiple menu items (only need to account for one of each item type)
    items = db.relationship("Menu", back_populates="tickets", secondary="customer_ticket_to_menu")
    