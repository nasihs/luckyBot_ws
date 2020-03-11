#!/usr/bin/python2

import socket
# import time
import struct

import cv2
import numpy as np


HOST = ''
PORT = 1201
BUFSIZE = 1024
ADDR = (HOST, PORT)


class CamRecv(object):

    def __init__(self, resolution=(640, 480)):
        self.resolution = resolution
        self.frame = None
        self.frame_bytes = None
        self.fps = 15

    def bytes_to_frame(self, bytes):
        pass

    def receive(self, address):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(address)
        sock.listen(5)
        conn, addr = sock.accept()
        print('Accept connnection from %s : %s' % addr)

        while True:
            info = struct.unpack(b'lhh', conn.recv(8))
            buffer_size = int(info[0])
            if buffer_size:
                try:
                    buffer = b''
                    temp_buffer = buffer
                    while buffer_size:
                        temp_buffer = conn.recv(buffer_size)
                        buffer_size -= len(temp_buffer)
                        buffer += temp_buffer
                    data = np.fromstring(buffer, dtype='uint8')
                    frame = cv2.imdecode(data, 1)
                    cv2.imshow('cam', frame)
                except Exception as e:
                    print(e.args)
                    pass
                finally:
                    if cv2.waitKey(10) == 27:  # 按ESC退出
                        sock.close()
                        cv2.destroyAllWindows()
                        print('Disconnected.')
                        break


if __name__ == '__main__':
    cam1 = CamRecv()
    cam1.receive(ADDR)
