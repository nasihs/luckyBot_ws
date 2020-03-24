#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""???-???
"""


from __future__ import print_function
import sys
import socket
import struct

import cv2
import numpy as np


HOST = '49.235.15.235'
PORT = 1201
ADDR = (HOST, PORT)


class CamRecv(object):

    def __init__(self, address):
        self.resolution = (320, 240)
        self.fps = 15

        self.address = address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # ????

        self.frame = ''
        self.frame_bytes = ''

    def receive(self):
        # self.sock.bind(self.address)
        # self.sock.listen(5)
        # conn, addr = self.sock.accept()
        print('Connecting to {0}:{1}...'.format(self.address[0], self.address[1]))
        self.sock.connect(self.address)
        # self.sock.send('OK')
        # print('Accept connnection from {0}:{1}'.format(addr[0], addr[1]))
        print(self.sock.recv(1024))  # ??????
        while True:
            tempdata = ''
            for i in range(8):
                tempdata += self.sock.recv(1)
                # if len(tempdata) == 0:
                #     continue
            info = struct.unpack('ihh', tempdata)
            buffer_size = int(info[0])
            if buffer_size:
                try:
                    buffer = ''
                    temp_buffer = buffer
                    while buffer_size:
                        temp_buffer = self.sock.recv(buffer_size)
                        buffer_size -= len(temp_buffer)
                        buffer += temp_buffer
                    data = np.fromstring(buffer, dtype='uint8')

                    self.frame = cv2.imdecode(data, 1)
                    cv2.imshow('Cam', self.frame)
                except Exception as e:
                    print(e.args)
                    cv2.destroyAllWindows()
                    break
                finally:
                    if cv2.waitKey(5) == 27:  # ESC
                        self.sock.close()
                        cv2.destroyAllWindows()
                        print('Esc.')
                        break


if __name__ == '__main__':
    host = '{0}'.format(sys.argv[1]) if len(sys.argv) > 1 else HOST
    cam1 = CamRecv((host, PORT))
    cam1.receive()
