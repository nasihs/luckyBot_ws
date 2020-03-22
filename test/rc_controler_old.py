#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""RC遥控车控制端
目标ip作为命令行参数传入 默认为 '192.168.50.88'

可以前进后退
"""


import sys
import socket
from pynput import keyboard


HOST = '192.168.50.88'
PORT = 1201
BUFSIZE = 1024
# ADDR = (HOST, PORT)


def on_press(key):
    global sock
    if key.char == 'w':
        sock.send(b'forward')
    elif key.char == 's':
        sock.send(b'back')
    elif key.char == 'a':
        sock.send(b'forward&left')
    elif key.char == 'd':
        sock.send(b'forward&right')
    elif key.char == 'p':
        sock.send(b'unlock')
    elif key.char == 'q':
        sock.send(b'quit')
        sock.close()
        return False


def on_release(key):
    global sock
    sock.send(b'stop')


host = '{0}'.format(sys.argv[1]) if len(sys.argv) > 1 else HOST
print('target server{0}:{1}'.format(host, PORT))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, PORT))
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
