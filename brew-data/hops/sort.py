#!/usr/bin/env python

f = open('hops.txt', 'r')
of = open('hops.csv', 'w')

for line in f:
    # print line
    line = line.rstrip()
    hopinf = line.split('  ');
    for inf in hopinf:
        if (inf != ''):
            print >>of, ("%s," % inf),

    print >>of, ("\n"),

