from flask import Flask
from flask_jwt_extended import JWTManager
from models import db
from auth import auth_blueprint  # Ensure this line is correct
from request_management import request_blueprint
from payment import payment_blueprint

app = Flask(__name__)

# Load configurations from config.py
app.config.from_object('config.Config')

# Initialize extensions
db.init_app(app)
jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(request_blueprint, url_prefix='/requests')
app.register_blueprint(payment_blueprint, url_prefix='/payment')

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True,port=5003)
