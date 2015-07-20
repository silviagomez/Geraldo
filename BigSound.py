#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Written by Kevin Cole <kjcole@novawebcoop.org> 2015.07.20

# Do something interesting with Xinda "Big Sound", a.k.a. Keyes KY-037
# Sensitive microphone sensor module. Documentation, such as it is can
# be found at:
#
# https://tkkrlab.nl/wiki/Arduino_KY-037_Sensitive_microphone_sensor_module

from pyb import *

# The Passive buzzer (black, no sticker) takes a modulated sigal.

buzzer = Pin("X1", Pin.OUT_PP)  # Passive buzzer

while True:
    for i in range(80):  # 2ms period = 500 Hz
        buzzer.high()
        delay(1)
        buzzer.low()
        delay(1)

    for i in range(100):  # 4ms period = 250 Hz
        buzzer.high()
        delay(2)
        buzzer.low()
        delay(2)

DO = Pin("X5", Pin.IN)  # Read the Digital Output
AO = ADC(Pin("X6"))     # Read the Analog Output

#A0.read()

#buffy = bytearray(10000)   # 10,000 samples...
#AO.read_timed(buffy, 100)  # ...over 100 seconds (100 samples / second)
