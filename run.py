from ext import create_app
from routes import*
# Initialize the Flask app
app = create_app()

# Run the app with the specified host and port
app.run(host="0.0.0.0", port=5000)