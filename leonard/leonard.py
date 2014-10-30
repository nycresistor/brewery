#!/usr/bin/env python  
 
"""
1951 Leonard Refrigerator Daemon
  -- target platform Intel Edison
"""

import mraa  
import time  
import sys
      
x = mraa.Gpio(2)  
z = mraa.Gpio(4)
x.dir(mraa.DIR_OUT)  
      
while True:  
    try:
        val = z.read()

        if ( val == 1 ):
            x.write(1)
        else:
            x.write(0)

        # print "%d" % val
       
    except:
        # print "dongs!"
        sys.exit(2)
