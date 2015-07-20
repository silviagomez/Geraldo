#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Initial version Written by Karanvir Dhillon, June 2015

# main.py -- put your code here!

try:
    from pyb import DAC
    from pyb import LED
    from pyb import Pin
    from pyb import USB_VCP

    sensitivity, maxn, minn = .5, 255, 0

    com = USB_VCP()
    light = DAC(2)
    y1, y2, y3 = Pin('Y1', Pin.IN), Pin('Y2', Pin.IN), Pin('Y3', Pin.IN)
    intensity, oldStr = maxn, str(y1.value()) + str(y2.value())

    directTab = {'1000': 1,
                 '0001': 1,
                 '0111': 1,
                 '1110': 1,
                 '1011': -1,
                 '1101': -1,
                 '0100': -1,
                 '0010': -1}

    def setByte(i):
        return i.to_bytes(1)

    def limitNums(num, maxn, minn):
        return max(minn, min(maxn, num))

    def handleLEDs(intensity, value):
        if intensity == maxn:
            LED(4).on()
            LED(1).off()
        elif intensity == minn:
            LED(1).on()
            LED(4).off()
        else:
            LED(1).off()
            LED(4).off()

        if value > 0 and intensity != maxn:
            LED(2).on()
            LED(3).off()
        elif value < 0 and intensity != minn:
            LED(3).on()
            LED(2).off()
        else:
            LED(2).off()
            LED(3).off()

    while True:
        v1, v2 = y1.value(), y2.value()
        currentStr = str(v1) + str(v2)
        usedStr = oldStr + currentStr
        oldStr = currentStr if directTab.get(usedStr) else oldStr

        additive = 0 if not directTab.get(usedStr) else directTab[usedStr] * sensitivity * (maxn - minn)/255
        intensity = limitNums(intensity + additive, maxn, minn)
        light.write_timed(setByte(round(intensity)), 1)

        print('Additive:', additive, 'Value:', intensity)
        handleLEDs(intensity, additive)

except BaseException as errStr:
    f = open('error.txt', 'w')
    f.write(str(errStr))
    f.close()
