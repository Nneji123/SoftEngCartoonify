from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, current_user

from PIL import Image
import base64

from models import db, Users
from utils import inference
from io import BytesIO
import numpy as np


home = Blueprint('home', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(home)

@home.route('/home', methods=['GET'])
@login_required
def show():
    return render_template('home.html')


@home.route('/upload', methods=['POST'])
@login_required
def upload_file():
    image = request.files['image']
    try:
        image.save(f"./static/{image.filename}")
        image_b64 = base64.b64encode(image.getvalue()).decode('utf-8')
        
        ref = Image.open(f"./static/{image.filename}")
        ref = np.asarray(ref)
        inference(ref)
    except PermissionError:
        return redirect(url_for('home.show') + '?error=permission-denied')
    
    # Car Image
    filename = str(current_user.id) + ".jpg"
    car_image = Image.open("./static/"+filename)
    buffer = BytesIO()
    car_image.save(buffer, "PNG")
    car_b64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    return render_template('display_image.html', image_b64=image_b64, car_b64=car_b64)
