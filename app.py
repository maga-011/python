from ext import create_app
from routes import register_routes

app = create_app()

# Register routes with the app
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
