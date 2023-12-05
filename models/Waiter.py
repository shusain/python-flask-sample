from dataclasses import dataclass
from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemyconfig import db

@dataclass
class Waiter(db.Model):
    # Waiter properties/property types, for JSON serialization
    id:int
    first_name:str
    last_name:str
    tax_number:str

    # Table columns to store properties
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    tax_number = Column(String)

    customerTicket = ForeignKey("customer_ticket.id")
    # Waiter can only serve on customer ticket