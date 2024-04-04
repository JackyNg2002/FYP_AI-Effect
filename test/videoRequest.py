import requests
import json
import time
# improt process
from threading import Thread
from multiprocessing import Process

from convertor import cv2_to_base64, base64_to_cv2
import cv2
import os
from request import send_request

port = os.getenv('PORT', 8000)
url = f"http://localhost:{port}/effect"


times=20

video=cv2.VideoCapture('asset/test.mp4')

cur_time = time.time()
for i in range(times):
  ret,frame=video.read()

  t = Thread(target=send_request,args=(frame,url))
  t.start()
  t.join()
  
for i in range(times):
  t.join()
print('fps: {:.2f}'.format(1/((time.time()-cur_time)/times)))
