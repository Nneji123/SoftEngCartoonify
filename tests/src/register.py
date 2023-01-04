from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import LoginManager
from models import Users, db
from werkzeug.security import generate_password_hash
import sqlalchemy

register = Blueprint("register", __name__, template_folder="./frontend")
login_manager = LoginManager()
login_manager.init_app(register)


@register.route("/register", methods=["GET", "POST"])
def show():
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

import pytest

def test_show(client):
    # Test that the registration form is displayed correctly
    response = client.get("/register")
    assert response.status_code == 200
    assert b"Username" in response.data
    assert b"Email" in response.data
    assert b"Password" in response.data
    assert b"Confirm Password" in response.data

    # Test that a new user is created and added to the database
    # with the correct hashed password when all fields are provided
    response = client.post(
        "/register",
        data={"username": "test_user", "email": "test@example.com", "password": "test_password", "confirm-password": "test_password"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    # Check that the new user has been added to the database and has the correct hashed password
    # ...

    # Test that an error is returned when the password and confirm password fields do not match
    response = client.post(
        "/register",
        data={"username": "test_user", "email": "test@example.com", "password": "test_password", "confirm-password": "incorrect_password"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"The password and confirm password fields do not match" in response.data

    # Test that an error is returned when any of the required fields are missing
    response = client.post(
        "/register",
        data={"username": "test_user", "email": "test@example.com", "password": "test_password"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Missing required fields" in response.data

