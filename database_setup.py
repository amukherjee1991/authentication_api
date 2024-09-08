from app import app
from models import db, User

with app.app_context():
    db.create_all()
    
    # Seed sample users
    if not User.query.filter_by(username='user1').first():
        user1 = User(username='user1', password='password123', package='Free')
        user2 = User(username='user2', password='password123', package='Prime')
        user3 = User(username='user3', password='password123', package='Ultra')
        db.session.add_all([user1, user2, user3])
        db.session.commit()

    print("Database initialized and users added!")
