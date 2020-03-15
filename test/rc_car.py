#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""局域网控制RC遥控车 被控端
"""


import sys
import socket
# from threading import Thread
from time import sleep


import Adafruit_PCA9685


HOST = ''
PORT = 1201
ADDR = (HOST, PORT)


class Vehicle(object):

    def __init__(self, channel_motor=0, channel_servo=3, freq=60):
        self._pwm = Adafruit_PCA9685.PCA9685()
        self._channel_motor = channel_motor
        self._channel_servo = channel_servo
        self._pwm.set_pwm_freq(freq)

    def sec_to_pulse(self, second):
        pass

    def unlock_esc(self):
        self._pwm.set_pwm(self._channel_motor, 0, 307)  # 电调解锁方式尚不明确
        sleep(2)
        self._pwm.set_pwm(self._channel_motor, 0, 375)  # 电调解锁方式尚不明确
        # 测试舵机
        self.turn(375)
        sleep(1)
        self._pwm.set_pwm(self._channel_servo, 0, 460)
        sleep(1)
        self._pwm.set_pwm(self._channel_servo, 0, 200)
        sleep(1)
        self._pwm.set_pwm(self._channel_servo, 0, 375)
        # print('unlock')
        # return True

    def run(self, pulse):
        self._pwm.set_pwm(self._channel_motor, 0, pulse)

    def stop(self):
        self._pwm.set_pwm(self._channel_motor, 0, 375)  # 375为停止
    # self._pwm.set_pwm(self._channel, 0, 185)

    def turn(self, pulse):
        self._pwm.set_pwm(self._channel_servo, 0, pulse)
        # print('turn')


port = '{0}'.format(sys.argv[1]) if len(sys.argv) > 1 else PORT
luckyBot = Vehicle()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, port))
    s.listen(5)
    print('waiting...')
    client, addr = s.accept()
    print('recevied connection from:{0}:{1}'.format(addr[0], addr[1]))
    temp_cmd = None
    while True:
        data = client.recv(1024)
        command = data.decode('utf-8')
        if temp_cmd != command:
            temp_cmd = command
            print(temp_cmd)
            if temp_cmd == 'unlock':
                luckyBot.unlock_esc()
            elif temp_cmd == 'forward':
                luckyBot.run(400)
            elif temp_cmd == 'back':
                luckyBot.run(300)
            elif temp_cmd == 'stop':
                luckyBot.stop()
            elif temp_cmd == 'turn_left':
                luckyBot.turn(460)
            elif temp_cmd == 'turn_right':
                luckyBot.turn(200)
            elif temp_cmd == 'servo_reset':
                luckyBot.turn(375)
            elif temp_cmd == 'quit':
                client.close()
                print('Quit.')
                break
