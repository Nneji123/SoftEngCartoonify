from flask import Blueprint, url_for, redirect
from flask_login import LoginManager, login_required, logout_user, current_user
import os

logout = Blueprint('logout', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(logout)

@logout.route('/logout')
@login_required
def show():
    if os.path.exists("static/"+str(current_user.id)+".jpg"):
        os.remove("static/"+str(current_user.id)+".jpg")
    else:
        pass
    logout_user()
    return redirect(url_for('login.show') + '?success=logged-out')