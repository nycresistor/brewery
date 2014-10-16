#!/usr/bin/env python

#from __future__ import print_function
import glob
import os

of = open('yeasts.csv', 'w')
yeasts = []

os.chdir(".")
for file in glob.glob("*.raw"):
    f = open(file, 'r')
    for line in f:
        line = line.rstrip() 
        yeastinf = line.split('  ');
        if ( yeastinf[0] in yeasts ):
            print yeastinf[0]
        else:
            print "yeast not found appending!"
            yeasts.append( yeastinf[0] ) 
            for inf in yeastinf:
                if (inf != ''):
                    print >>of, ("%s," % inf),

            print >>of, ("\n"),
    f.close()

of.close()
