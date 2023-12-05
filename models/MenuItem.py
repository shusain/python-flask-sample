from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemyconfig import db

@dataclass
class MenuItem(db.Model):
    item_name: str
    description: str
    price: float

    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    description = Column(String)
    price = Column(Numeric)

    tickets = db.relationship("CustomerTicket", back_populates="items", secondary="customer_ticket_to_menu")