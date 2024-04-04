import requests
import json
import time
from threading import Thread
import cv2

from request import send_request

url = "http://localhost:80/effect"



image=cv2.imread('asset/bus.jpg')

times=40

cur_time = time.time()
for i in range(times):
  t = Thread(target=send_request,args=(image,url))
  t.start()
  
for i in range(times):
  t.join()
print('fps: {:.2f}'.format(1/((time.time()-cur_time)/times)))
