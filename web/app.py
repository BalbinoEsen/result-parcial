from flask import Flask
from routes.main_routes import MainRoutes
from routes.person_routes import PersonRoutes

app = Flask(__name__)
MainRoutes.configure_routes(app)
PersonRoutes.configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
