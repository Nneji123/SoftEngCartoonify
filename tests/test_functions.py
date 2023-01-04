from ..src.utils import preprocess_image, inference_test
from PIL import Image
import os
import numpy as np
# import sys
# sys.path.insert(0, '../src')
from ..src.models import Users

location = os.path.join(os.path.dirname(__file__), 'test.jpg')
model = os.path.join(os.path.dirname(__file__), 'model.onnx')


# my_file = (location / 'test.jpg').resolve()

def test_inference():
    image = Image.open(location)
    inference_test(image, model)
    assert os.path.exists("output.jpg")
    os.remove("output.jpg")
    
## write a function to test the preprocess_image function
def test_preprocess_image():
    image = Image.open(location)
    image = preprocess_image(image)
    assert image.shape == (1, 120, 168, 3)
    assert image.dtype == np.float32
    assert image.min() >= -1.0
    assert image.max() <= 1.0
    
def test_users():
    user = Users(
        username="test_user",
        email="test@example.com",
        password="test_password",
    )
    assert user.username == "test_user"
    assert user.email == "test@example.com"
    assert user.password == "test_password"


# def test_home_page(app, client):
#     """
#     GIVEN a Flask application configured for testing
#     WHEN the '/' page is requested (GET)
#     THEN check that the response is valid
#     """
#     response = client.get('/')
#     assert response.status_code == 200

# # write a function to test if the database is connected
# from ..src.models import db
# import sqlalchemy

# def test_db():
#     db.create_all()
#     assert True
