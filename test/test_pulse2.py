#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""测试pulse
将pwm.set_pwm()放在while循环中的效果
"""


# from time import sleep
import Adafruit_PCA9685


pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

pulse = int(input('input pulse:'))
while True: 
    pwm.set_pwm(0, 0, pulse)
