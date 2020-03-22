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
frame_array = np.array(frame)
frame_bytes = frame_array.tostring()
data = np.frombuffer(frame_bytes)
frame1 = cv2.imdecode(data, 1)
cv2.imshow('cam', frame1)
cv2.waitKey(0)
cv2.destroyAllWindows()
