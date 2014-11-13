Leonard
=======

This is software used to run the Intel Edison that is used
as the brains of the NYC Resistor beer fridge.

The refrigerator is a 1951 Leonard.

Feature Goals
-------------

temp control {
  * rtd pt100 sensor
  * ambient temperature thermistor
}

  * multiple relays 110v 10-20amp
  * ceramic heater ( maybe )
  * 100 lb flex sensor
  * 2 ( maybe 3 ) solenoid valves



to pre-empt systemd on uboot with edison:

setenv bootargs_debug $bootargs_debug init=/bin/sh
