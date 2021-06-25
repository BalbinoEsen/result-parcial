from flask import render_template


class LogProcessRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/login")
        def login():
            return render_template("login.html")
