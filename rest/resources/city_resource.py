from flask_restful import Resource, reqparse
from logic.city_logic import CityLogic


class City(Resource):
    def __init__(self):
        self.city_put_args = self.createParser()
        self.logic = CityLogic()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("Name", type=str, help="name of the city")
        args.add_argument("CountryCode", type=str, help="country code of the city")
        args.add_argument("District", type=str, help="district of the city")
        args.add_argument("Population", type=int, help="population of the city")
        return args

    def get(self, id):
        result = self.logic.getCityById(id)
        return result, 200

    def post(self, id):
        cityDict = self.logic.getCityById(id)
        countryCode = cityDict["CountryCode"]
        result = self.logic.getCityByCountryCode(countryCode)
        return result, 200

    def put(self, id):
        city = self.city_put_args.parse_args()
        rows = self.logic.insertCity(city)
        return {"rowsAffected": rows}

    def patch(self, id):
        city = self.city_put_args.parse_args()
        rows = self.logic.updateCity(id, city)
        return {"rowsAffected": rows}

    def delete(self, id):
        city = self.city_put_args.parse_args()
        rows = self.logic.deleteCity(id)
        return {"rowsAffected": rows}
