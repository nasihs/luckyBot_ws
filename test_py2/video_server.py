#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""图传 服务端
"""

from __future__ import print_function
import socket
# import threading


HOST = ''
PORT = 1201
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
# 分别接收两个客户端
print('Waiting for client1...')
conn1, addr1 = s.accept()
conn1.send('Connected.')
print('Accept connection from %s : %s..' % addr1)
print('Waiting for client1...')
conn2, addr2 = s.accept()
conn2.send('Connected.')
print('Accept connection from %s : %s..' % addr2)
conn1.setblocking(0)
conn2.setblocking(0)
# 开始处理消息
while True:
    try:
        temp1 = conn1.recv(4096)
        conn2.send(temp1)
    except Exception as e:
        # print(e.args)
        pass

    try:
        temp2 = conn2.recv(4096)
        conn1.send(temp2)
    except Exception as e:
        # print(e.args)
        pass

print('Done')
