from flask import render_template, redirect, request
import requests


class DashboardRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/dashboard")
        def dashboard():
            return render_template("dashboard.html")

        @app.route("/dashboard/city/<int:id>")
        def city(id):
            url = f"http://localhost:23512/city/{id}"
            response = requests.get(url)
            if response.status_code == 200:
                dataJson = response.json()
                return render_template("city.html", id=id, city=dataJson)
            else:
                return redirect("dashboard")

        @app.route("/dashboard/country/<int:id>")
        def country(id):
            url = f"http://localhost:23512/city/{id}"
            response = requests.post(url)
            if response.status_code == 200:
                dataJson = response.json()
                return render_template("country.html", cityList=dataJson)
            else:
                return redirect("dashboard")

        @app.route("/dashboard/city/create", methods=["GET", "POST"])
        def cityCreate():
            if request.method == "GET":
                return render_template("cityCreate.html")
            elif request.method == "POST":
                url = f"http://localhost:23512/city/0"
                print(url)
                data = {
                    "Name": request.form["name"],
                    "CountryCode": request.form["countrycode"],
                    "District": request.form["district"],
                    "Population": int(request.form["population"]),
                }
                print(data)
                response = requests.put(url, data=data)
                print(response)
                if response.status_code == 200:
                    dataJson = response.json()
                    return f"rowsAffected by create: {dataJson['rowsAffected']}"
                else:
                    return redirect("dashboard")
