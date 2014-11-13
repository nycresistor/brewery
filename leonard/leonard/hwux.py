#!/usr/bin/env python  
 
"""
1951 Leonard Refrigerator Daemon
  -- target platform Intel Edison
  -- temp sensor    a0
  -- switch         d4
  -- relay          d2
  -- rtd            spi
"""

import getopt
import mraa
import sys
import time

def get_switch(sid):
    z = mraa.Gpio(sid)
    val = z.read()
    return val

