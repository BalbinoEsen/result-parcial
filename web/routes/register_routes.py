from flask import render_template, request, redirect
from tools.recaptcha_helper import RecaptchaHelper
from logic.user_logic import UserLogic


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

                    # verificar que el usuario sea unico
                    logic = UserLogic()
                    username = request.form["user"]
                    result = logic.getRowByUser(username)
                    if len(result) == 0:
                        return "register validRecaptcha uniqueUser post"
                    else:
                        redirect("register")

                else:
                    redirect("register")
