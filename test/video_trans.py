#!/usr/bin/python2
# -*- coding: utf-8 -*-


from __future__ import print_function
import socket
import time
import struct

import cv2
import numpy as np


HOST = '49.235.15.235'
PORT = 1201
BUFSIZE = 1024
ADDR = (HOST, PORT)


class MyCamera(object):

    def __init__(self, resolution=(640, 480)):
        self.resolution = resolution
        self.frame = None
        self.frame_bytes = None
        self.fps = 15

    def frame_to_bytes(self, frame):
        param = [int(cv2.IMWRITE_JPEG_QUALITY), self.fps]
        _, frame_encode = cv2.imencode('.jpg', frame, param)
        frame_array = np.array(frame_encode)
        return frame_array.tostring()

    def send(self, address):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 设置复用
        sock.connect(address)
        # print(sock.recv())  # 显示连接成功
        cap = cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)

        while True:
            time.sleep(0.1)
            _, frame = cap.read()
            frame = cv2.resize(frame, self.resolution)
            # 本地窗口显示
            cv2.imshow("cam", frame)
            if cv2.waitKey(10) == 27:
                sock.close()
                cap.release()
                cv2.destroyAllWindows()
                break

            frame_bytes = self.frame_to_bytes(frame)
            try:
                packet = struct.pack(b'lhh', len(frame_bytes), self.resolution[0], self.resolution[1])
                sock.send(packet + frame_bytes)
                # sock.send(frame_bytes)
            except Exception as e:
                print(e.args)
                sock.close()
                cap.release()
                return


if __name__ == '__main__':
    cam1 = MyCamera()
    cam1.send(ADDR)
