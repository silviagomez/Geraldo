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

# The chromatic scale is based on the 12th root of 2 = 1.0594630943592952645

halfstep  = 1.0594630943592952645
wholestep = halfstep * halfstep

fundemental = 440.0
pitch = {}
pitch["C4"] = fundemental * wholestep * wholestep * halfstep
pitch["D4"] = pitch["C4"] * wholestep
pitch["E4"] = pitch["D4"] * wholestep
pitch["F4"] = pitch["E4"] * halfstep
pitch["G4"] = pitch["F4"] * wholestep
pitch["A4"] = pitch["G4"] * wholestep
pitch["B4"] = pitch["A4"] * wholestep
pitch["C5"] = pitch["B4"] * halfstep

scale = (pitch["C4"],
         pitch["D4"],
         pitch["E4"],
         pitch["F4"],
         pitch["G4"],
         pitch["A4"],
         pitch["B4"],
         pitch["C5"])

buzzer = Pin("X1", Pin.OUT_PP)  # Passive buzzer

while True:
    for note in scale:
        for duration in range(100):
            buzzer.high()
            udelay(int(500000.0 / note))
            buzzer.low()
            udelay(int(500000.0 / note))
        print(int(500000.0 / note))
        delay(200)

# while True:
#     for i in range(80):  # 2ms period = 500 Hz
#         buzzer.high()
#         delay(1)
#         buzzer.low()
#         delay(1)
#
#     for i in range(100):  # 4ms period = 250 Hz
#         buzzer.high()
#         delay(2)
#         buzzer.low()
#         delay(2)

# DO = Pin("X5", Pin.IN)  # Read the Digital Output
# AO = ADC(Pin("X6"))     # Read the Analog Output

# A0.read()

# buffy = bytearray(10000)   # 10,000 samples...
# AO.read_timed(buffy, 100)  # ...over 100 seconds (100 samples / second)
