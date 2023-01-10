import base64
import os
import shutil
from io import BytesIO

import numpy as np
from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import LoginManager, current_user, login_required
import PIL
from PIL import Image
from utils import inference



home = Blueprint("home", __name__, template_folder="./frontend")
login_manager = LoginManager()
login_manager.init_app(home)


@home.route("/home", methods=["GET"])
@login_required
def show():
    
    if current_user.is_authenticated:
        return render_template("home.html")
    else:
        return redirect(url_for("login.show"))


@home.route("/upload", methods=["POST"])
@login_required
def upload_file():
    """
    The upload_file function is used to upload an image file and then run the inference function on it.
    It takes in a request object, which contains information about the HTTP request sent by the client.
    The function checks if there is already a folder for this user's id, and deletes it if so.
    Then it creates a new folder with that user's id as its name, saves the uploaded image into that directory,
    and runs inference on that image.

    Args:

    Returns:
        A rendered template that displays the image and car
    """
    image = request.files["image"]
    try:
        if os.path.exists(f"./static/{str(current_user.id)}/"):
            shutil.rmtree(f"./static/{str(current_user.id)}/")
        else:
            pass
        os.mkdir(f"./static/{str(current_user.id)}")
        try:
            image.save(f"./static/{str(current_user.id)}/{image.filename}")
        except (IsADirectoryError, PIL.UnidentifiedImageError, FileNotFoundError):
            flash("Please upload a valid image file")
            shutil.rmtree(f"./static/{str(current_user.id)}/")
        
        # resize the uploaded image
        image_b64 = Image.open(f"./static/{(current_user.id)}/{image.filename}")
        buffers = BytesIO()
        image_b64.save(buffers, "PNG")
        
        image_b64 = base64.b64encode(buffers.getvalue()).decode("utf-8")
        
        
        ref = Image.open(f"./static/{(current_user.id)}/{image.filename}")
        ref = np.asarray(ref)
        inference(ref)
    except (PermissionError, PIL.UnidentifiedImageError, FileNotFoundError):
        flash("Please upload a valid image file")
        return redirect(url_for("home.show") + "?error=permission-denied")

    # Car Image
    filename = str(current_user.id) + ".jpg"
    car_image = Image.open(f"./static/{(current_user.id)}/{filename}")
    buffer = BytesIO()
    car_image.save(buffer, "PNG")
    car_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return render_template("display_image.html", image_b64=image_b64, car_b64=car_b64)
