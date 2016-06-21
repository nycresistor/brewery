#!/usr/bin/env python
'''
    relay interaction module
'''

import mraa
import time
import os
import zmq
import sys
import random

def tap_relay(rid, stime):
    ntime = get_stime()
    if (ntime > (stime + 400)):
        x = mraa.Gpio(rid)
        x.dir(mraa.DIR_OUT)
        x.write(1)
        stime = get_stime()
    return stime

def untap_relay(rid, stime):
    ntime = get_stime()
    if (ntime > (stime + 400)):
        x = mraa.Gpio(rid)
        x.dir(mraa.DIR_OUT)
        x.write(0)
        stime = get_stime()
    return stime

def read_gpio(rid):
    x = mraa.Gpio(rid)
    value = x.read()
    return value

