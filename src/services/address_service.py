from flask import jsonify
from src.models.address_model import AddressModel
from src.config.settings import db

def create_address(user_id, addresses):
    results = []
    try:
        for item in addresses:
            address = item.get('address')
            name = item.get('name')
            contact = item.get('contact')

            # Validate required fields
            if not all([address, name, contact]):
                results.append({"error": "Missing required fields", "item": item})
                continue

            # Create and save the address
            new_address = AddressModel(user_id=user_id, address=address, name=name, contact=contact)
            db.session.add(new_address)
            db.session.commit()

            # Add the successfully created address to results
            results.append(new_address.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    return jsonify(results), 201

def get_address_by_user(user_id):
    addresses = AddressModel.query.filter_by(user_id=user_id).all()
    if not addresses:
        return jsonify({"error": "Address not found"}), 404
    return jsonify({ "data": [address.to_dict() for address in addresses]}), 200

def get_address_by_id(id, user_id):
    address = AddressModel.query.filter_by(id=id, user_id=user_id).first()
    if not address:
        return jsonify({"error": "Address not found"}), 404
    return jsonify([address.to_dict()]), 200

def update_address_by_id(id, user_id, addresses):
    results = []
    try:
        for item in addresses:
            # Extract data from the request
            new_address = item.get('address')
            name = item.get('name')
            contact = item.get('contact')

            # Validate required fields
            if not all([new_address, name, contact]):
                results.append({"error": "Missing required fields", "item": item})
                continue

            # Query the address to update
            address = AddressModel.query.filter_by(id=id, user_id=user_id).first()
            if not address:
                results.append({"error": "Address not found", "item": item})
                continue

            # Update the fields
            address.address = new_address
            address.name = name
            address.contact = contact

            # Commit the changes
            db.session.commit()

            # Add the successfully updated address to results
            results.append(address.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    return jsonify(results), 200

def delete_address_by_id(id, user_id):
    address = AddressModel.query.filter_by(id=id, user_id=user_id).first()
    if not address:
        return jsonify({"error": "Address not found"}), 404
    db.session.delete(address)
    db.session.commit()
    return jsonify({ "message": "Address deleted successfully"}), 200

def set_main_address(id, user_id):
    others_main_address = AddressModel.query.filter_by(user_id=user_id, is_main=True).first()
    if others_main_address:
        others_main_address.is_main = False
        
    address = AddressModel.query.filter_by(id=id, user_id=user_id).first()
    if not address:
        return jsonify({"error": "Address not found"}), 404
    address.is_main = True
    db.session.commit()
    return jsonify({ "message": "Address set as main successfully"}), 200