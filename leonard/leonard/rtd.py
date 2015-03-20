#!/usr/bin/env python

import mraa

while(1):
    x = mraa.Gpio(7)
    x.dir(mraa.DIR_OUT)
    x.write(1)
    print x
