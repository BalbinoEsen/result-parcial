from flask import render_template


def configure_person_routes(app):
    pass

    @app.route("/person")
    def person():
        return render_template("person.html")
