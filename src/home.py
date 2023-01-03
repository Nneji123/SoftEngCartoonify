import base64
import os
import shutil
from io import BytesIO

import numpy as np
from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import LoginManager, current_user, login_required
from models import Users, db
from PIL import Image
from utils import inference

home = Blueprint("home", __name__, template_folder="./frontend")
login_manager = LoginManager()
login_manager.init_app(home)


@home.route("/home", methods=["GET"])
@login_required
def show():
    return render_template("home.html")


@home.route("/upload", methods=["POST"])
@login_required
def upload_file():
    image = request.files["image"]
    try:
        if os.path.exists(f"./static/{str(current_user.id)}/"):
            shutil.rmtree(f"./static/{str(current_user.id)}/")
        os.mkdir(f"./static/{str(current_user.id)}")
        image.save(f"./static/{str(current_user.id)}/{image.filename}")
        image_b64 = base64.b64encode(image.getvalue()).decode("utf-8")

        ref = Image.open(f"./static/{(current_user.id)}/{image.filename}")
        ref = np.asarray(ref)
        inference(ref)
    except PermissionError:
        return redirect(url_for("home.show") + "?error=permission-denied")

    # Car Image
    filename = str(current_user.id) + ".jpg"
    car_image = Image.open(f"./static/{(current_user.id)}/{filename}")
    buffer = BytesIO()
    car_image.save(buffer, "PNG")
    car_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return render_template("display_image.html", image_b64=image_b64, car_b64=car_b64)
