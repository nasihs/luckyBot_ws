#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""发送图片 测试功能
"""

from __future__ import print_function
import sys
import socket
# import time
import struct

import cv2
import numpy as np


HOST = '192.168.50.3'
PORT = 1201
ADDR = (HOST, PORT)


class PicSender(object):

    def __init__(self, address):
        self.resolution = (300, 300)
        self.frame = None
        self.address = address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def frame_to_bytes(self, frame):
        param = [int(cv2.IMWRITE_JPEG_QUALITY), self.fps]
        _, frame_encode = cv2.imencode('.jpg', frame, param)
        frame_array = np.array(frame_encode)
        return frame_array.tostring()

    def send(self, frame):
        print('connecting to:{0}:{1}'.format(self.address[0], self.address[1]))
        try:
            self.connect(self.address)
            print(self.sock.recv(1024))
        except Exception as e:
            print('connection failed', e.args)
            self.sock.close()
            return

        frame = cv2.resize(frame, self.resolution)
        frame_bytes = self.frame_to_bytes(frame)
        while True:
            try:
                # python2的string为bytes类型 不需要b''转换
                packet = struct.pack('lhh', len(frame_bytes), self.resolution[0], self.resolution[1])
                self.sock.send(packet + frame_bytes)
            except Exception as e:
                print('send failed', e.args)
                self.sock.close()
                # cap.release()
                return


if __name__ == '__main__':
    # img_path = sys.argv[1]
    host = '{0}'.format(sys.argv[1]) if len(sys.argv) > 1 else HOST
    frame = cv2.imread('./3.jpg')
    ps = PicSender((host, PORT))
    ps.send(frame)
