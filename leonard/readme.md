Leonard
=======

This is software used to run the Intel Edison that is used
as the brains of the NYC Resistor beer fridge.

The refrigerator is a 1951 Leonard.

Application
-----------

/bin/temp  -- queries for temp status from rtdd / zmqd

boot order :

sbin/zmqd - zeromq queue daemon
sbin/rtdd - rtd sensor monitoring daemon
sbin/lcdd - lcd driver daemon
sbin/mrcd - mechanical relay control daemon
 
