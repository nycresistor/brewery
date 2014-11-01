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
import time
import sys

__version__ = "0.1"
app_name = "Leonard Daemon"

def get_temp(aid):
    y = mraa.Aio(aid)
    t = y.read()
    resistance=(float)(1023-t)*10000/t
    ctemp=(float)(1/(log(resistance/10000)/3975+1/298.15)-273.15)
    ftemp=ctemp*9/5+32
    return ftemp

def tap_relay(rid):
    x = mraa.Gpio(rid)
    x.dir(mraa.DIR_OUT)
    x.write(1)
    return 0

def untap_relay(rid):
    x = mraa.Gpio(rid)
    x.dir(mraa.DIR_OUT)
    x.write(0)
    return 0

def get_switch(sid):
    z = mraa.Gpio(sid)
    val = z.read()
    return val

def usage():
    print "some usage info would be nice wouldn't it?"
    return 0


def main():

    # Grab command line arguments
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ht:v", ["help", "temp="])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)
    output = None
    verbose = False

    for o, a in opts:
        if o == "-v":
            verbose = True
            print "%s - %s" % (app_name, __version__)
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif t in ("-t", "--temp"):
            tempformat = a
        else:
            assert False, "unhandled option"
    if (tempformat):
        try:
            ftemp = get_temp(0)
            print ftemp
        except getopt.GetoptError, err:
            print str(err)
            sys.exit(2)

    else:
        sys.exit(2)


if __name__ == "__main__":
    main()

