#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""发送图片 测试功能
"""


from __future__ import print_function
import socket
import struct

import cv2
import numpy as np


HOST = ''
PORT = 1201
BUFSIZE = 1024
ADDR = (HOST, PORT)


class CamRecv(object):

    def __init__(self):
        self.resolution = (300, 300)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def recv(self, address):
        self.sock.bind(address)
        self.sock.listen(5)
        conn, addr = self.sock.accept()
        conn.send('connected to reciever.')
        print('Accept connection from {0}:{1}'.format(conn, addr))

        while True:
            info = struct.unpack('lhh', conn.recv(8))
            buffer_size = int(info[0])
            if buffer_size:
                print('图片大小为:{0}bytes'.format(buffer_size))
                try:
                    buffer = ''
                    temp_buffer = buffer
                    while buffer_size:
                        temp_buffer = conn.recv(buffer_size)
                        buffer_size -= len(temp_buffer)
                        buffer += temp_buffer
                    data = np.frombuffer(buffer)
                    frame = cv2.imdecode(data, 1)
                    cv2.imshow('cam', frame)
                except Exception as e:
                    print(e.args)
                    conn.close()
                    cv2.destroyAllWindows()
                    break
                finally:
                    if cv2.waitKey(10) == 27:
                        conn.close()
                        cv2.destroyAllWindows()
                        print('Esc.')
                        break


if __name__ == '__main__':
    cam1 = CamRecv()
    cam1.recv(ADDR)

