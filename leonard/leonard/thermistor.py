#!/usr/bin/env python  
 
"""
Thermistor Sensor Methods
"""

import mraa
import sys
import time

from math import log

def get_temp(aid):
    y = mraa.Aio(aid)
    t = y.read()
    resistance=(float)(1023-t)*10000/t
    ctemp=(float)(1/(log(resistance/10000)/3975+1/298.15)-273.15)
    ftemp=ctemp*9/5+32
    return ftemp

