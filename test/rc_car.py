#!/usr/bin/python3
# -*- coding: utf-8 -*-


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

    def unlock_esc(self):
        self._pwm.set_pwm(self._channel_motor, 0, 307)  # 电调解锁方式尚不明确
        sleep(2)
        # print('unlock')
        return True

    def run(self, pulse):
        self._pwm.set_pwm(self._channel_motor, 0, pulse)

    def stop(self):
        self._pwm.set_pwm(self._channel_motor, 0, 307)
    # self._pwm.set_pwm(self._channel, 0, 185)

    def turn(self, pulse=300):
        print('turn')


luckyBot = Vehicle()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(ADDR)
    s.listen(5)
    print('waiting...')
    client, addr = s.accept()
    print('connected.')
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
                luckyBot.run(407)
                pass
            elif temp_cmd == 'forward&left':
                pass
            elif temp_cmd == 'forward&right':
                pass
            elif temp_cmd == 'back':
                pass
            elif temp_cmd == 'stop':
                luckyBot.stop()
                pass
            elif temp_cmd == 'quit':
                break
