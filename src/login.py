import os

from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import LoginManager, login_user
from werkzeug.security import check_password_hash
from oauthlib.oauth2 import WebApplicationClient
import requests
import json


from dotenv import load_dotenv
from models import Users, GooogleUsers

load_dotenv()

login = Blueprint(
    "login", __name__, template_folder="./frontend", static_folder="../frontend"
)
login_manager = LoginManager()
login_manager.init_app(login)

client = WebApplicationClient(os.getenv("GOOGLE_CLIENT_ID"))

def get_google_provider_cfg():
    return requests.get(os.getenv("GOOGLE_DISCOVERY_URL")).json()

@login.route("/login/google")
def login_google():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

@login.route("/login/google/callback")
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
        users_email = userinfo_response.json()["email"]
    else:
        return "User email not available or not verified by Google.", 400

    user = GooogleUsers.query.filter_by(email=users_email).first()
    if user:
        login_user(user)
        return redirect(url_for("home.show") + "?success=login-successful")
    else:
        flash("You are not registered with us. Please register first.")
        return redirect(url_for("register.show") + "?error=user-not-found")




@login.route("/login", methods=["GET", "POST"])
def show():
    """
    The show function renders the login page. If a user is already logged in, they are redirected to the home page.
    If a user is not logged in, and they submit their username and password, if it matches what's on file for that
    username, then they will be redirected to the home page.

    Returns:
        The home page if the user is logged in, or the login page if the user is not logged in.
    """
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = Users.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                if user.is_admin:
                    login_user(user, remember=True)
                    return redirect(url_for("admin.show"))
                else:
                    login_user(user)
                    next_page = request.args.get('next')
                    flash("You are logged in.")
                    return redirect(next_page) if next_page else redirect(url_for('home.show'))
            else:
                flash("Incorrect password. Please try again.")
                return redirect(url_for("login.show") + "?error=incorrect-password")
        else:
            flash("You are not registered with us. Please register first.")
            return redirect(url_for("login.show") + "?error=user-not-found")
    else:
        return render_template("register_and_login.html")
