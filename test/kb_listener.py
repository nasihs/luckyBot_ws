#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""键盘监听程序
"""

from pynput import keyboard


def on_press(key):
    print(key.char)


def on_release(key):
    print('key_up')


a = 333
# 监听键盘按键
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
