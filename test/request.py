import cv2
import requests
import json

from convertor import cv2_to_base64


headers = {
  'Content-Type': 'application/json'
}

def send_request(frame,url):
    # resize frame to 384x640
    frame = cv2.resize(frame, (640, 640))

    image=cv2_to_base64(frame)
    print(len(image)/1024,"KB")
    payload = json.dumps({
        "image": image,
        "effect": "detect"
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    # result.append(base64_to_cv2(response.json()['annotated_images'][0]))
    # print('fps: {:.2f}'.format(1/(time.time()-cur_time)))
