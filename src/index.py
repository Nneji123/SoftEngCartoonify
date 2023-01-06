from flask import Blueprint, redirect

index = Blueprint("index", __name__, template_folder="./frontend")


@index.route("/", methods=["GET"])
def show():
    """
    The show function renders the home page of the application.
    """
    return redirect("login")
