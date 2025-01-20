from flask_login import UserMixin
from ext import db, login_manager

class User(UserMixin, db.Model):  # Inherit from UserMixin
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)  # Username should be unique
    password = db.Column(db.String(128), nullable=False)  # Increased length for hashed password
    mail = db.Column(db.String(120), unique=True, nullable=False)  # Email should be unique
    phone_number = db.Column(db.String(15), nullable=False)  # Increased length for international formats

    def __repr__(self):
        return f"<User {self.username}>"

class Feedback(db.Model):
    __tablename__ = 'feedbacks'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), nullable=False)  # Use username as a reference
    feedback = db.Column(db.Text, nullable=False)  # Feedback is typically long text

    def __repr__(self):
        return f"<Feedback {self.username}: {self.feedback}>"


    def __repr__(self):
        return f"<Feedback by {self.username}>"

# User loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Query user by ID
