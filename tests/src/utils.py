import os

import cv2
import numpy as np
import onnxruntime as ort
from PIL import Image

_sess_options = ort.SessionOptions()
_sess_options.intra_op_num_threads = os.cpu_count()
MODEL_SESS = ort.InferenceSession(
    "model.onnx", _sess_options, providers=["CPUExecutionProvider"]
)

from flask_login import current_user


def preprocess_image(image: Image) -> np.ndarray:
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    h, w, c = np.shape(image)
    if min(h, w) > 720:
        if h > w:
            h, w = int(720 * h / w), 720
        else:
            h, w = 720, int(720 * w / h)
    image = cv2.resize(image, (w, h), interpolation=cv2.INTER_AREA)
    h, w = (h // 8) * 8, (w // 8) * 8
    image = image[:h, :w, :]
    image = image.astype(np.float32) / 127.5 - 1
    return np.expand_dims(image, axis=0)


def inference(image: np.ndarray) -> Image:
    image = preprocess_image(image)
    results = MODEL_SESS.run(None, {"input_photo:0": image})
    output = (np.squeeze(results[0]) + 1.0) * 127.5
    output = np.clip(output, 0, 255).astype(np.uint8)
    filename = str(current_user.id) + ".jpg"
    cv2.imwrite("./static/" + f"{str(current_user.id)}/" + filename, output)
    # os.remove("instance/image.jpg")
    return "Output Saved!"

def inference_test(image: np.ndarray) -> Image:
    image = preprocess_image(image)
    results = MODEL_SESS.run(None, {"input_photo:0": image})
    output = (np.squeeze(results[0]) + 1.0) * 127.5
    output = np.clip(output, 0, 255).astype(np.uint8)
    cv2.imwrite("output.jpg", output)
    # os.remove("instance/image.jpg")
    return "Output Saved!"
## write a function to test the inference function

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