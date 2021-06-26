from flask import render_template, request, redirect
from tools.recaptcha_helper import RecaptchaHelper


class RegisterRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/register", methods=["GET", "POST"])
        def register():
            if request.method == "GET":
                return render_template("register.html")
            elif request.method == "POST":
                recHelper = RecaptchaHelper(request)
                if recHelper.validateRecaptcha():
                    return "register valid post"
                else:
                    redirect("register")
