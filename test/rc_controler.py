#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import socket
from pynput import keyboard


HOST = '192.168.50.88'
PORT = 1201
BUFSIZE = 1024
ADDR = (HOST, PORT)


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


if not sys.argv == sys.argv[0]:
    host = '{0}'.format(sys.argv[1])
else:
    host = '192.168.50.88'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, PORT))
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()