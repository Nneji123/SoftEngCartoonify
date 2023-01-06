from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import LoginManager, login_user
from werkzeug.security import check_password_hash

from models import Users, db

login = Blueprint(
    "login", __name__, template_folder="./frontend", static_folder="../frontend"
)
login_manager = LoginManager()
login_manager.init_app(login)


@login.route("/login", methods=["GET", "POST"])
def show():
    """
    The show function renders the login page. If a user is already logged in, they are redirected to the home page.
    If a user is not logged in, and they submit their username and password, if it matches what's on file for that
    username, then they will be redirected to the home page.

    Args:

    Returns:
        The register and login page
    """
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = Users.query.filter_by(username=username).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("home.show"))
            else:
                return redirect(url_for("login.show") + "?error=incorrect-password")
        else:
            return redirect(url_for("login.show") + "?error=user-not-found")
    else:
        return render_template("register_and_login.html")
