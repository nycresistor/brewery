#!/usr/bin/env python

import pyupm_i2clcd as lcd
#

def plcd(strlcd):
    x = lcd.Jhd1313m1(0, 0x3E, 0x62)
    x.write(strlcd)


