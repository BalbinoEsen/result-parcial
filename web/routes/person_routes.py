from flask import render_template


class PersonRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/person")
        def person():
            return render_template("person.html")
