import socket
import cv2
import numpy as np
import time
from custom_socket import CustomSocket
import json

img = cv2.imread("../pic/test1.jpg")
print(img.shape)
img = cv2.resize(img, (1080,720))

# host = socket.gethostname()
host = "192.168.10.79"
port = 10001

c = CustomSocket(host,port)
c.clientConnect()
result = c.whatIsThat(img)
# print(result)
print(result['bboxs'][0]['y'])

