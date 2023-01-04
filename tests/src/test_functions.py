from utils import preprocess_image, inference_test
from PIL import Image
import os
import numpy as np
from models import Users

def test_inference():
    image = Image.open("test.jpg")
    inference_test(image)
    assert os.path.exists("output.jpg")
    os.remove("output.jpg")
    
## write a function to test the preprocess_image function
def test_preprocess_image():
    image = Image.open("test.jpg")
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