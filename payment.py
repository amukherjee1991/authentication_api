from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User, db

payment_blueprint = Blueprint('payment', __name__)

@payment_blueprint.route('/payment_page', methods=['GET'])
def payment_page():
    # Simulate a payment page (for real cases, integrate with a payment gateway like Stripe)
    return jsonify({"msg": "You've reached your request limit. Please upgrade your plan."}), 402

@payment_blueprint.route('/upgrade', methods=['POST'])
@jwt_required()
def upgrade_package():
    current_user = get_jwt_identity()['username']
    user = User.query.filter_by(username=current_user).first()
    new_package = request.json.get('new_package', None)
    
    if new_package not in ['Free', 'Prime', 'Ultra']:
        return jsonify({"msg": "Invalid package selected"}), 400
    
    user.package = new_package
    user.reset_requests()  # Reset requests when upgrading
    db.session.commit()
    
    return jsonify({"msg": f"Package upgraded to {new_package}"}), 200
