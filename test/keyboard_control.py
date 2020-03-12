#!/usr/bin/python3
# -*- coding: utf-8 -*-


from time import sleep

import Adafruit_PCA9685
from pynput import keyboard


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

    def run(self, pulse=407):
        print('run')
        pass

    def stop(self):
        print('stop')
        # self._pwm.set_pwm(self._channel, 0, 185)
        pass

    def turn(self, pulse=300):
        print('turn')
        pass


car1 = Vehicle()
current_key = None


def on_press(key):
    global current_key
    if key.char != current_key:
        current_key = key.char
        if key.char == 'w':
            car1.run()
        elif key.char == 's':
            car1.run()
        elif key.char == 'a':
            car1.turn()
        elif key.char == 'd':
            car1.turn()
        elif key.char == 'q':  # 电调解锁
            car1.unlock_esc()
    elif key.char == current_key:
        pass


def on_release(key):
    if key.char == 'w':
        car1.stop()
    elif key.char == 's':
        car1.stop()


# 监听键盘按键
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
