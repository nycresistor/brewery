#!/usr/bin/env python

import getopt
import fcntl
import mraa
import serial
import socket
import string
import struct
import sys
import time

import pyupm_i2clcd as lcd



__version__ = "0.1"
app_name = "mechanical relay switch daemon"

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

def tap_relay(rid):
    x = mraa.Gpio(rid)
    x.dir(mraa.DIR_OUT)
    x.write(1)
    return 0

def untap_relay(rid):
    x = mraa.Gpio(rid)
    x.dir(mraa.DIR_OUT)
    x.write(0)
    return 0

def read_gpio(rid):
    x = mraa.Gpio(rid)
    value = x.read()
    return value

untap_relay(2)

def readrtd():
    ser = serial.Serial('/dev/ttyUSB0', 115200)
    while True:
        celsius = ser.readline()
        celsius = celsius.rstrip()

        try:
            celsius = float(celsius)

            relay_state = read_gpio(2)
            relay_state = int(relay_state)

            if (celsius > 27):
                if (relay_state == 0):
                    tap_relay(2)
            else:
                if (relay_state == 1):
                    untap_relay(2)
            
            fahrenheit = 9.0/5.0 * celsius + 32
            myLcd.clear()
            myLcd.setColor(255, 255, 0)
            myLcd.setCursor(0,0)
            temp_line = "%d C / %d F - %s" % (celsius, fahrenheit, relay_state)
            myLcd.write(temp_line)
            myLcd.setCursor(1, 0)
            ip_address = get_ip_address('wlan0')
            myLcd.write(ip_address)
        except:
            print "oof : %s" % celsius
    ser.close()

readrtd()

