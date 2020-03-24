#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""?? ???
"""


from __future__ import print_function
import socket
import struct

import cv2
import numpy as np


HOST = ''
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
        self.sock.bind(self.address)
        self.sock.listen(5)
        conn, addr = self.sock.accept()
        conn.send('OK')
        print('Accept connnection from {0}:{1}'.format(addr[0], addr[1]))

        while True:
            tempdata = self.conn.recv(8)
            if len(tempdata) == 0:
                print('+1')
                continue
            info = struct.unpack('ihh', tempdata)
            buffer_size = int(info[0])
            if buffer_size:
                try:
                    buffer = ''
                    temp_buffer = buffer
                    while buffer_size:
                        temp_buffer = conn.recv(buffer_size)
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
    cam1 = CamRecv(ADDR)
    cam1.receive()
