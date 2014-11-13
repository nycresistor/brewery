#!/usr/bin/env python  
 
"""
1951 Leonard Refrigerator Daemon
  -- target platform Intel Edison
  -- temp sensor    a0
  -- switch         d4
  -- relay          d2
  -- rtd            spi
"""

import mraa
import sys
import time

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


