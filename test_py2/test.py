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
cv2.imshow('cam', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
