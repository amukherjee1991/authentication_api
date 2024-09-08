from flask import Blueprint, jsonify, redirect
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User, db
from datetime import datetime, timedelta

request_blueprint = Blueprint('requests', __name__)

@request_blueprint.route('/check', methods=['GET'])
@jwt_required()
def check_requests():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()
    
    # Check if requests need resetting
    if datetime.utcnow() > user.request_reset_date + timedelta(days=30):
        user.reset_requests()
    
    # Define request limits
    package_limits = {'Free': 3, 'Prime': 100, 'Ultra': float('inf')}
    
    # Check if user has exceeded their limit
    if user.requests_made >= package_limits[user.package]:
        # If the user is at their limit, prompt them for payment
        return redirect('/payment/payment_page')
    
    # Update request count
    user.requests_made += 1
    db.session.commit()
    
    return jsonify({"msg": "Request successful", "requests_remaining": package_limits[user.package] - user.requests_made})
