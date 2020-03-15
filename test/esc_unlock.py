#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""电调解锁
pulse 307，持续2s
"""

import time
import Adafruit_PCA9685


# Uncomment to enable debug output.
# import logging
# logging.basicConfig(level=logging.DEBUG)

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)
pwm.set_pwm(0, 0, 307)
time.sleep(2)
