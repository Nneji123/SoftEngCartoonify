import sqlalchemy
from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

from models import Users, db

register = Blueprint("register", __name__, template_folder="./frontend")
login_manager = LoginManager()
login_manager.init_app(register)


@register.route("/register", methods=["GET", "POST"])
def show():
    """
    The show function renders the register_and_login.html template, which contains a form for registering or logging in.
    If the user is already logged in, they are redirected to their profile page.

    Args:

    Returns:
        The register_and_login.html template
    """
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm-password"]

        if username and email and password and confirm_password:
            if password == confirm_password:
                hashed_password = generate_password_hash(password, method="sha256")
                try:
                    new_user = Users(
                        username=username,
                        email=email,
                        password=hashed_password,
                    )

                    db.session.add(new_user)
                    db.session.commit()
                except sqlalchemy.exc.IntegrityError:
                    return redirect(
                        url_for("register.show") + "?error=user-or-email-exists"
                    )

                return redirect(url_for("login.show") + "?success=account-created")
        else:
            return redirect(url_for("register.show") + "?error=missing-fields")
    else:
        return render_template("register_and_login.html")
