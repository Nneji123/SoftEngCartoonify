import os
import shutil

from flask import Blueprint, redirect, url_for
from flask_login import LoginManager, current_user, login_required, logout_user

logout = Blueprint("logout", __name__, template_folder="./frontend")
login_manager = LoginManager()
login_manager.init_app(logout)


@logout.route("/logout")
@login_required
def show():
    if os.path.exists(f"./static/{str(current_user.id)}"):
        shutil.rmtree(f"./static/{str(current_user.id)}")
    else:
        pass
    logout_user()
    return redirect(url_for("login.show") + "?success=logged-out")