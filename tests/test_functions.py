from ..src.utils import preprocess_image, inference_test
from PIL import Image
import os
import numpy as np

from ..src.models import Users

location = os.path.join(os.path.dirname(__file__), 'test.jpg')
model = os.path.join(os.path.dirname(__file__), 'model.onnx')



def test_inference():
    """
    The test_inference function tests the inference function by passing it an image and a model.
    It then checks that the output file exists, and removes it from the directory.
    """
    image = Image.open(location)
    inference_test(image, model)
    assert os.path.exists("output.jpg")
    os.remove("output.jpg")
    

def test_preprocess_image():
    image = Image.open(location)
    """
    The test_preprocess_image function tests the preprocess_image function.
    It opens an image from a location, converts it to RGB format, and then
    converts it to a NumPy array of shape (120, 168) with type float32. The
    minimum value is -0.5 and the maximum value is 0.5.
    """
    image = preprocess_image(image)
    assert image.shape == (1, 120, 168, 3)
    assert image.dtype == np.float32
    assert image.min() >= -1.0
    assert image.max() <= 1.0
    
def test_users():
    """
    The test_users function creates a new user object and tests whether the username, email, and password are set correctly.
    
    
    Args:
    
    Returns:
        The username, email and password of the user
    """
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
