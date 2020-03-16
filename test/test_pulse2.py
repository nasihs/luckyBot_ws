#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""测试pulse
将pwm.set_pwm()放在while循环中的效果
"""


# from time import sleep
# import sys

import Adafruit_PCA9685


pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

channel = int(input('input channel'))
pulse = int(input('input pulse:'))
print('channel:{0} pulse:{1}'.format(channel, pulse))
# channel, pulse = '{0}'.format(sys.argv[1]) if len(sys.argv) > 1 else 0, 375

pwm.set_pwm(channel, 0, pulse)
