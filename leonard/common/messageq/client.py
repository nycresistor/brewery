#!/usr/bin/env python
''' 
    0mq client methods
'''

import zmq
import random

def get_temp():
    client_port = "5559"
    client_context = zmq.Context()
    client_socket = client_context.socket(zmq.REQ)
    client_socket.connect ("tcp://localhost:%s" % client_port)
    client_id = random.randrange(1,10005)
    client_socket.RCVTIMEO = 5000 
    try:
        client_socket.send ("templs %s" % client_id)
        celsius = client_socket.recv().rstrip()
    except:
        return "FAIL"
    try:
        return float(celsius)
    except (ValueError, TypeError):
        return celsius

