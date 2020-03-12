#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""测试pulse
"""


# from time import sleep
import Adafruit_PCA9685


pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

pulse = int(input('input pulse:'))
pwm.set_pwm(0, 0, pulse)
