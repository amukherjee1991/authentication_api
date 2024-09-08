from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

tier_blueprint = Blueprint('tier', __name__)

@tier_blueprint.route('/communicate', methods=['GET'])
@jwt_required()
def communicate():
    # Get the current user's identity from the JWT token
    current_user = get_jwt_identity()
    user_tier = current_user['tier']

    # Check user tier and perform actions accordingly
    if user_tier == 'Free':
        return jsonify({"msg": "Access limited. Upgrade to Prime or Ultra for more features."}), 403
    elif user_tier == 'Prime':
        # Example: Call another endpoint or service (mocked here)
        return jsonify({"msg": "Data fetched from the Prime API endpoint."}), 200
    elif user_tier == 'Ultra':
        # Example: Call another, more privileged endpoint or service (mocked here)
        return jsonify({"msg": "Data fetched from the Ultra API endpoint."}), 200
    else:
        return jsonify({"msg": "Invalid user tier."}), 400
