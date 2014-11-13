#!/usr/bin/env python  
 
"""
   Relay Firing Methods
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


