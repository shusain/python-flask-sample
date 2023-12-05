from flask import jsonify, request
from flaskapp import app
from models.MenuItem import MenuItem
from sqlalchemyconfig import db


# Menu Item Routes
@app.route("/menu", methods=["GET"])
def menu_item_list():
    menu_items = MenuItem.query.all()
    return jsonify(menu_items)

@app.route("/menu", methods=["POST"])
def menu_item_create():
    content = request.get_json()

    menu_item = MenuItem(
        item_name=content["item_name"],
        description=content["description"],
        price=content["price"]
    )

    db.session.add(menu_item)
    db.session.commit()

    return jsonify({ "success": True })