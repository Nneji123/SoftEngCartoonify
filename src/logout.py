import os
import shutil

from flask import Blueprint, redirect, url_for, flash
from flask_login import LoginManager, current_user, login_required, logout_user

logout = Blueprint("logout", __name__, template_folder="./frontend")
login_manager = LoginManager()
login_manager.init_app(logout)


@logout.route("/logout")
@login_required
def show():
    """
    The show function is used to log out the user and delete their folder in static.
    It redirects them back to the login page with a success message.

    Args:

    Returns:
        A redirect to the login page with a query parameter of success=logged-out
    """
    if os.path.exists(f"./static/{str(current_user.id)}"):
        shutil.rmtree(f"./static/{str(current_user.id)}")
    else:
        pass
    logout_user()
    flash("You have successfully logged out!", "success")
    return redirect(url_for("login.show") + "?success=logged-out")
