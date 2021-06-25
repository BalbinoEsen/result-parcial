from flask import Flask
from routes.main_routes import configure_main_routes
from routes.person_routes import configure_person_routes

app = Flask(__name__)
configure_main_routes(app)
configure_person_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
