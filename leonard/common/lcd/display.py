#!/usr/bin/env python
# matt@nycresistor.com

import getopt
import fcntl
import random
import socket
import string
import struct
import sys
import time

import pyupm_i2clcd as lcd


# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
myLcd.clear()
myLcd.setColor(255, 255, 0)
myLcd.setCursor(0,0)

def lcdloop(string1, string2):
    try:
        myLcd.clear()
        myLcd.setColor(255, 255, 0)
        myLcd.setCursor(0,0)
        myLcd.write(string1)
        myLcd.setCursor(1, 0)
        myLcd.write(string2)
    except:
        print "oof : %s" % celsius

