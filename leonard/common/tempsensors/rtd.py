#!/usr/bin/env python

import zmq
import mraa
import serial
import time
import sys
import random

port = "5560"
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:%s" % port)
server_id = random.randrange(1,10005)
# ser = serial.Serial('/dev/ttyUSB0', 115200)

def serial_data(port, baudrate):
    ser = serial.Serial(port, baudrate, timeout=10)

    while True:
        ser.flush()
        ser.flushInput()
        yield ser.readline()

    ser.close()

def poll_temperature():
    for line in serial_data('/dev/ttyUSB0', 115200):
        message = socket.recv()
        celsius = line
        celsius = celsius.rstrip()
        try:
            celsius = bytes(celsius)
        except:
            print "oof : %s" % celsius
        time.sleep (1) 
        socket.send(celsius)
    ser.close()
    return celsius
