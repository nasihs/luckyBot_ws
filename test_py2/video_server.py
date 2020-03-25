#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""中转服务器 将video_sender发送的数据转发给video_reciever
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
        """每次转发1024
        每次转发一字节，但运行1-2分钟后报 coorupt JPEG data 错误
        还是图片数据不完整的问题
        """
        temp1 = conn1.recv(1)
        conn2.send(temp1)
    except Exception as e:
        # print(e.args)
        pass

    try:
        temp2 = conn2.recv(1)
        conn1.send(temp2)
    except Exception as e:
        # print(e.args)
        pass

print('Done')
