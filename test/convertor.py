import base64
import cv2
import numpy as np

def cv2_to_base64(image):
    _, buffer = cv2.imencode('.jpg', image)
    image_bytes = buffer.tobytes()
    base64_bytes = base64.b64encode(image_bytes)
    base64_string = base64_bytes.decode('utf-8')
    return base64_string

def base64_to_cv2(base64_string):
    base64_bytes = base64_string.encode('utf-8')
    image_bytes = base64.b64decode(base64_bytes)
    buffer = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(buffer, cv2.IMREAD_COLOR)
    return image