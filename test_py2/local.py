#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""本地图片编码解码测试
"""


from __future__ import print_function
# import sys
# import socket
# import struct

import cv2
import numpy as np


frame = cv2.imread('./3.jpg')
param = [int(cv2.IMWRITE_JPEG_QUALITY), 15]
_, frame_encode = cv2.imencode('.jpg', frame, param)
frame_array = np.array(frame_encode)
frame_bytes = frame_array.tostring()

print('len(frame_bytes)=', len(frame_bytes))
data = np.fromstring(frame_bytes, dtype=np.uint8)
frame1 = cv2.imdecode(data, 1)
cv2.imshow('cam', frame1)
cv2.waitKey(0)
cv2.destroyAllWindows()
