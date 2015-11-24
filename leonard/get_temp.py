#!/usr/bin/env python

import getopt
import fcntl
import serial
import socket
import string
import struct
import sys

import pyupm_i2clcd as lcd

__version__ = "0.1"
app_name = "rtd temp reader"

# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
myLcd.clear()
myLcd.setColor(255, 255, 0)
myLcd.setCursor(0,0)

def get_ip_address(ifname):

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def readrtd():
    ser = serial.Serial('/dev/ttyUSB0', 115200)
    while True:
        celsius = ser.readline()
        celsius = celsius.rstrip()
        try:
            celsius = float(celsius)
            fahrenheit = 9.0/5.0 * celsius + 32
            myLcd.clear()
            myLcd.setColor(255, 255, 0)
            myLcd.setCursor(0,0)
            temp_line = "%d C / %d F" % (celsius, fahrenheit)
            myLcd.write(temp_line)
            myLcd.setCursor(1, 0)
            ip_address = get_ip_address('wlan0')
            myLcd.write(ip_address)
        except:
            print "oof : %s" % celsius
    ser.close()

readrtd()

