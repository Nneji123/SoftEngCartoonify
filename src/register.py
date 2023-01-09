import os

import sqlalchemy
from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import LoginManager
from werkzeug.security import generate_password_hash
from oauthlib.oauth2 import WebApplicationClient
import requests
import json
import sqlalchemy


from models import Users, db, GooogleUsers

from dotenv import load_dotenv

load_dotenv()


register = Blueprint("register", __name__, template_folder="./frontend")
login_manager = LoginManager()
login_manager.init_app(register)


client = WebApplicationClient(os.getenv("GOOGLE_CLIENT_ID"))

def get_google_provider_cfg():
    return requests.get(os.getenv("GOOGLE_DISCOVERY_URL")).json()

@register.route("/register/google")
def register_google():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

@register.route("/register/google/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code,
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(os.getenv("GOOGLE_CLIENT_ID"), os.getenv("GOOGLE_CLIENT_SECRET")),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that we have tokens (yay) let's find and hit URL
    # from Google that gives you user's profile information,
    # including their Google Profile Image and Email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # We want to make sure their email is verified.
    # The user authenticated with Google, authorized our
    # app, and now we've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    # Create a user in our db with the information provided
    # by Google
    # user = GooogleUsers(username=users_name, email=users_email)

    # Doesn't exist? Add to database
    user = bool(Users.query.filter_by(email=users_email).first())
    print(user)
    google_user = bool(GooogleUsers.query.filter_by(email=users_email).first())
    print(google_user)
    if user == False and google_user == False:
        try:
            new_user = GooogleUsers(id=unique_id, username=users_name, email=users_email, profile_pic=picture)
            db.session.add(new_user)
            db.session.commit()
            flash("You have successfully registered!", "success")
            return redirect(url_for("login.show") + "?success=account-created")
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
            flash("User already exists!", "failure")
            return redirect(url_for("register.show") + "?error=user-or-email-exists")
        finally:
            db.session.close()
    elif user == True or google_user == True:
        flash("User already exists!", "failure")
        return redirect(url_for("register.show") + "?error=user-or-email-exists")
        
    # Send user back to homepage




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
                user = bool(Users.query.filter_by(email=email).first())
                print(user)
                google_user = bool(GooogleUsers.query.filter_by(email=email).first())
                print(google_user)
                if user == False and google_user == False:
                    try:
                        new_user = Users(
                            username=username,
                            email=email,
                            password=hashed_password,
                        )

                        db.session.add(new_user)
                        db.session.commit()
                        flash("You have successfully registered!", "success")
                        return redirect(url_for("login.show") + "?success=account-created")
                    except sqlalchemy.exc.IntegrityError:
                        db.session.rollback()
                        flash("User already exists!", "failure")
                        return redirect(
                            url_for("register.show") + "?error=user-or-email-exists"
                        )
                    finally:
                        db.session.close()
                elif user or google_user:
                    flash("User already exists!", "failure")
                    return redirect(url_for("register.show") + "?error=user-or-email-exists")
        else:
            flash("Please fill in all fields!", "failure")
            return redirect(url_for("register.show") + "?error=missing-fields")
    else:
        return render_template("register_and_login.html")
