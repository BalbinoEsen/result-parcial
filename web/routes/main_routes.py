from flask import render_template


def configure_main_routes(app):
    pass

    @app.route("/")
    def home():
        return render_template("index.html")
