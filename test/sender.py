#!/usr/bin/python2
# -*- coding: utf-8 -*-
# https://zhuanlan.zhihu.com/p/80614707


from __future__ import print_function
import socket
import struct
import time
import cv2
import numpy


class Config(object):
    def __init__(self):
        self.TargetIP = ('192.168.50.2', 6666)
        self.resolution = (640, 480)  # 分辨率
        self.img_fps = 15  # each second send pictures
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect(self.TargetIP)
        self.img = ''
        self.img_data = ''

    def RT_Image(self):
        camera = cv2.VideoCapture(0)
        img_param = [int(cv2.IMWRITE_JPEG_QUALITY), self.img_fps]

        while True:
            time.sleep(0.1)  # sleep for 0.1 seconds
            _, self.img = camera.read()

            self.img = cv2.resize(self.img, self.resolution)

            _, img_encode = cv2.imencode('.jpg', self.img, img_param)
            img_code = numpy.array(img_encode)
            self.img_data = img_code.tostring() # bytes data
            try:
                packet = struct.pack(b'lhh', len(self.img_data), self.resolution[0], self.resolution[1])
                self.server.send(packet)
                self.server.send(self.img_data)
            except Exception as e:
                print(e.args)
                camera.release()
                return


if __name__ == '__main__':
    config = Config()
    config.RT_Image()
