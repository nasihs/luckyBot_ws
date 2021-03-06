#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""RC遥控车控制端
目标ip作为命令行参数传入 默认为 '192.168.50.88'
P: 解锁
W A S D: 方向键
Q: 退出
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
        sock.send(b'turn_left')
    elif key.char == 'd':
        sock.send(b'turn_right')
    elif key.char == 'p':
        sock.send(b'unlock')
    elif key.char == 'q':
        sock.send(b'quit')
        sock.close()
        return False


def on_release(key):
    global sock
    if key.char == 'w' or key.char == 's':
        sock.send(b'stop')
    elif key.char == 'a' or key.char == 'd':
        sock.send(b'servo_reset')


host = '{0}'.format(sys.argv[1]) if len(sys.argv) > 1 else HOST
print('target server{0}:{1}'.format(host, PORT))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, PORT))
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
