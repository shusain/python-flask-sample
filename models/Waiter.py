from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemyconfig import db

class Waiter(db.Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    tax_number = Column(String)

    customerTicket = ForeignKey("customer_ticket.id")
    # Waiter can only serve on customer ticket