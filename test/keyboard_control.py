#!/usr/bin/python3
# -*- coding: utf-8 -*-


from time import sleep
from threading import Thread

import Adafruit_PCA9685
from pynput import keyboard


w_is_pressed = None
a_is_pressed = None
s_is_pressed = None
d_is_pressed = None


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

    def turn(self, pulse=300):
        print('turn')


def on_press(key):
    global w_is_pressed
    global a_is_pressed
    global s_is_pressed
    global d_is_pressed

    if key.char == 'w':
        w_is_pressed = True
    elif key.char == 'a':
        a_is_pressed = True
    elif key.char == 's':
        s_is_pressed = True
    elif key.char == 'd':
        d_is_pressed = True
    elif key == keyboard.Key.esc:  # 停止监听
        return False


def on_release(key):
    global w_is_pressed
    global a_is_pressed
    global s_is_pressed
    global d_is_pressed

    if key.char == 'w':
        w_is_pressed = False
    elif key.char == 'a':
        a_is_pressed = False
    elif key.char == 's':
        s_is_pressed = False
    elif key.char == 'd':
        d_is_pressed = False


def control():
    global w_is_pressed
    global a_is_pressed
    global s_is_pressed
    global d_is_pressed

    while True:
        if w_is_pressed:
            car1.run()
        else:
            car1.stop()
        if s_is_pressed:
            car1.run()
        else:
            car1.stop()
        if a_is_pressed:
            car1.turn()
        else:
            print('reset')
        if d_is_pressed:
            car1.turn
        else:
            print('reset')


car1 = Vehicle()

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
controler = Thread(target=control)
listener.start()
controler.start()

# 监听键盘按键
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#    listener.join()
