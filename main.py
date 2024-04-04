from fastapi import FastAPI
from typing import List, Union
from pydantic import BaseModel
import base64
import cv2
import numpy as np
from ultralytics import YOLO

# Load a model
models={
    "detect":YOLO('model/yolov8n.pt') ,
    "classify":YOLO('model/yolov8n-cls.pt'),
    "pose":YOLO('model/yolov8n-pose.pt'),
    "segment":YOLO('model/yolov8n-seg.pt')
}

for model in models.values():
    model(source='main.jpg',verbose=False,half=False)

app = FastAPI()

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

class Item(BaseModel):
    image: str
    effect: str

@app.post('/effect')
async def effect(item:Item):
    # Get the base64 encoded image from the request
    image_data = item.image
    effect = item.effect

    model=models[effect]
    image = base64_to_cv2(image_data)
    results=model(image,verbose=True)
    for result in results:
        image = result.plot()

    encoded_image_data = cv2_to_base64(image)
    response = {'image': encoded_image_data}
    return response
