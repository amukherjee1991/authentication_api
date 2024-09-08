from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import User, db

# Define the Blueprint
auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    
    user = User.query.filter_by(username=username).first()
    if user is None or user.password != password:
        return jsonify({"msg": "Bad username or password"}), 401
    
    # Include the user's tier in the JWT token
    access_token = create_access_token(identity={"username": username, "tier": user.package})
    return jsonify(access_token=access_token), 200
