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

def get_temp(aid):
    y = mraa.Aio(aid)
    t = y.read()
    resistance=(float)(1023-t)*10000/t
    ctemp=(float)(1/(log(resistance/10000)/3975+1/298.15)-273.15)
    ftemp=ctemp*9/5+32
    return ftemp

