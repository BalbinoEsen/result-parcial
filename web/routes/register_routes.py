from flask import render_template


class RegisterRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/register")
        def register():
            return render_template("register.html")
