from ext import create_app, db
from models import User, Feedback

app = create_app()

with app.app_context():
    # Create the database and tables if they don't exist
    db.create_all()
