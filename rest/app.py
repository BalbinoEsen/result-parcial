from flask import Flask
from flask_restful import Api
from resources.city_resource import City

app = Flask(__name__)
api = Api(app)

api.add_resource(City, "/city/<int:id>")

if __name__ == "__main__":
    app.run(debug=True, port=23512)
