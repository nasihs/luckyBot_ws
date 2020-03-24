#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""图传 发送端
支持接收端ip作为命令行参数传入 默认 HOST = '192.168.50.3'
"""


from __future__ import print_function
import sys
import socket
import time
import struct

import cv2
import numpy as np


HOST = '192.168.50.3'
PORT = 1201
BUFSIZE = 1024
# ADDR = (HOST, PORT)


class MyCamera(object):

    def __init__(self, address):
        self.resolution = (320, 240)
        self.fps = 15

        self.address = address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 设置复用

        self.frame = ''
        self.frame_bytes = ''

    def send(self):
        print('Connecting to {0}:{1}...'.format(self.address[0], self.address[1]))
        self.sock.connect(self.address)
        print(self.sock.recv(1024))  # 显示连接成功

        cap = cv2.VideoCapture(0)
        param = [int(cv2.IMWRITE_JPEG_QUALITY), self.fps]

        while True:
            time.sleep(0.1)
            _, self.frame = cap.read()
            self.frame = cv2.resize(self.frame, self.resolution)
            # 本地窗口显示
            # cv2.imshow("cam", self.frame)
            _, frame_encode = cv2.imencode('.jpg', self.frame, param)
            frame_array = np.array(frame_encode)
            self.frame_bytes = frame_array.tostring()

            try:
                packet = struct.pack(b'lhh', len(self.frame_bytes), self.resolution[0], self.resolution[1])
                self.sock.send(packet)
                self.sock.send(self.frame_bytes)
            except Exception as e:
                print(e.args)
                self.sock.close()
                cap.release()
                return

            if cv2.waitKey(10) == 27:
                self.sock.close()
                self.cap.release()
                cv2.destroyAllWindows()
                break


if __name__ == '__main__':
    # 接收端ip作为命令行参数传入
    host = '{0}'.format(sys.argv[1]) if len(sys.argv) > 1 else HOST
    # print('target:{0}:{1}'.format(host, PORT))
    cam1 = MyCamera((host, PORT))
    cam1.send()
