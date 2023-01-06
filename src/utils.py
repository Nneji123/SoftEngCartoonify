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
    """
    The preprocess_image function takes an image as input and returns a preprocessed image.
    The preprocessed image is in the form of a numpy array, with shape (batch_size, h, w, c).
    The function performs the following steps:
        1) Convert RGB to BGR.
        2) Resize the input image to size (h', w'), where max(h',w') == 720 and min(h',w') == 64.
           If min(h', w') &gt; 720 or max(h' ,w') &lt; 64 raise an error. The aspect ratio

    Args:
        image: Image: Pass the image to the preprocess_image function

    Returns:
        A numpy array of shape (batch_size, h, w, c) that represents the preprocessed image
    """

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
    """
    The inference_test function takes an image and a model location as input,
    and returns the output of the inference. The function also saves the output to a file called &quot;output.jpg&quot;.

    Args:
        image: Image: Pass the image to be processed by the model
        model_location: str: Store the location of the model file

    Returns:
        The output of the model
    """

    image = preprocess_image(image)
    results = MODEL_SESS.run(None, {"input_photo:0": image})
    output = (np.squeeze(results[0]) + 1.0) * 127.5
    output = np.clip(output, 0, 255).astype(np.uint8)
    filename = str(current_user.id) + ".jpg"
    cv2.imwrite("./static/" + f"{str(current_user.id)}/" + filename, output)
    # os.remove("instance/image.jpg")
    return "Output Saved!"


def inference_test(image: Image, model_location: str) -> Image:
    image = preprocess_image(image)
    results = ort.InferenceSession(
        model_location, _sess_options, providers=["CPUExecutionProvider"]
    ).run(None, {"input_photo:0": image})
    output = (np.squeeze(results[0]) + 1.0) * 127.5
    output = np.clip(output, 0, 255).astype(np.uint8)
    cv2.imwrite("output.jpg", output)
    return "Output Saved!"
