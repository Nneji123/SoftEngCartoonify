from ..src.utils import preprocess_image, inference_test
from PIL import Image
import os
import numpy as np
from ..src.models import Users
from pathlib import Path

location = os.path.join(os.path.dirname(__file__), 'test.jpg')
# my_file = (location / 'test.jpg').resolve()

def test_inference():
    image = Image.open(location)
    inference_test(image)
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


# def test_home_page():
#     """
#     GIVEN a Flask application configured for testing
#     WHEN the '/' page is requested (GET)
#     THEN check that the response is valid
#     """
#     flask_app = create_app('flask_test.cfg')

#     # Create a test client using the Flask application configured for testing
#     with flask_app.test_client() as test_client:
#         response = test_client.get('/')
#         assert response.status_code == 200
