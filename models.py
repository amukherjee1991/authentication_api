from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    package = db.Column(db.String(20), nullable=False, default='Free')  # 'Free', 'Prime', 'Ultra'
    requests_made = db.Column(db.Integer, default=0)
    request_reset_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def reset_requests(self):
        self.requests_made = 0
        self.request_reset_date = datetime.utcnow()
        db.session.commit()
