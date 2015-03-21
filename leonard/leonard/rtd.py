#!/usr/bin/env python

import mraa

sout = mraa.Gpio(6)
sout.dir(mraa.DIR_OUT)

sin = mraa.Gpio(7)
sin.dir(mraa.DIR_IN)

# x.write(1)
# print x
while(1):
    seven = sin.read()
    if ( seven == 1 ):
        print "HIGH!"
    else:
        print "LOW"

