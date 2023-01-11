import os

import sqlalchemy
from dotenv import load_dotenv

from flask import Flask, render_template
from flask_login import LoginManager

from home import home
from index import index
from login import login
from logout import logout
from models import Users, db, GooogleUsers
from register import register
from admin import admin
from init_db import create_admin

load_dotenv()


app = Flask(__name__, static_folder="./frontend/static")


POSTGRES = os.getenv("POSTGRES")
SQLITE = os.getenv("SQLITE")
DATABASE_MODE = os.getenv("DATABASE_MODE")
SECRET_KEY = os.getenv("SECRET_KEY")


app.config["SECRET_KEY"] = SECRET_KEY

if DATABASE_MODE == "postgres":
    app.config["SQLALCHEMY_DATABASE_URI"] = POSTGRES
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLITE

login_manager = LoginManager()
login_manager.init_app(app)
# login_manager.login_view = "home.show"
db.init_app(app)
app.app_context().push()

app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(register)
app.register_blueprint(home)
app.register_blueprint(admin)
# login_manager.login_view = 'login'


@login_manager.user_loader
def load_user_user(user_id):
    """
    The load_user_user function is used to load a user from the database. It takes in a user_id and returns either a 
    Users object or GooogleUsers object depending on which one exists in the database. If neither exist, it returns None.
    
    Args:
        user_id: Get the user object from the database
    
    Returns:
        A user object
    """
    myuser = Users.query.get(user_id)
    googleuser = GooogleUsers.query.get(user_id)
    try:
        if myuser:
            return myuser
        if googleuser:
            return googleuser
    except (sqlalchemy.exc.OperationalError) as e:
        return render_template("error.html", e="Database not found")
 

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    create_admin()
    app.run(port=os.getenv("PORT", default=5000), debug=os.getenv("DEBUG", default=True))#  ssl_context='adhoc', 
