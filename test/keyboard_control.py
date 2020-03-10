#!/usr/bin/python3

import time

import Adafruit_PCA9685
from pynput import keyboard


class Motor(object):
    def __init__(self, channel, freq):
        self._pwm = Adafruit_PCA9685.PCA9685()
        self._pwm.set_pwm_freq(freq)
        self._channel = channel

    def run(self, pulse):
        self._pwm.set_pwm(self._channel, 0, pulse)

    def stop(self):
        self._pwm.set_pwm(self._channel, 0, 185)


class Servo(object):
    def __init__(self, channel, freq):
        self._pwm = Adafruit_PCA9685.PCA9685()
        self._pwm.set_pwm_freq(freq)
        self._channel = channel
    
    def turn(self, direction):
        if direction == 'left':
            print('Left')
            pass
        else:
            print('Right')
            pass
    


def on_press(key):
    if key.char == 'i':
        print()


def on_release(key):
    print('key_up')


# 监听键盘按键
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()