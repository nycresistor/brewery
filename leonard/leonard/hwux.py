#!/usr/bin/env python  
 
"""
Hard Ware User eXperience
   how pushing all zee buttons does all zee things
"""

import getopt
import mraa
import sys
import time

def get_switch(sid):
    z = mraa.Gpio(sid)
    val = z.read()
    return val

