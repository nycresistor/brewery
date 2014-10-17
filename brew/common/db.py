#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _mysql
import json
import MySQLdb as mdb
import os
import re
import sys
import time
import traceback

def mysql_conn():
    print "this needs to be where we actually grab mysql configs and connect / test connection"

def mysql_init():
    con = mdb.connect('localhost', 'brew', 'brew', 'brew');

    with con:
        # grab connection reference
        cur = con.cursor()
        # initialize recipe table
        cur.execute("DROP TABLE IF EXISTS recipes")
        cur.execute("CREATE TABLE recipes(batch-id INT PRIMARY KEY AUTO_INCREMENT, \
                     batch-name VARCHAR(25), \
                     grainbill-id INT, \
                     hopsch-id INT, \
                     dryhopsch-id INT, \
                     yeast-id INT, \
                     mash-id INT, \
                     gravity-id INT, \
                     refiner-id INT)")

        # Initialize grainbills table
        cur.execute("DROP TABLE IF EXISTS grainbills")
        cur.execute("CREATE TABLE grainbills(grainbill-id INT PRIMARY KEY AUTO_INCREMENT, \
                     grainbill-name VARCHAR(25))")

        # Initialize grains table
        cur.execute("DROP TABLE IF EXISTS grains")
        cur.exectue("CREATE TABLE grains(grain-id INT PRIMARY KEY AUTO_INCREMENT, \
                     grain-name VARCHAR(25), \
                     region-id INT, \
                     grain-malter VARCHAR(25), \
                     grain-color VARCHAR(25), \
                     grain-region VARCHAR(25))")

        # Initialize hops table
        cur.execute("DROP TABLE IF EXISTS hops")
        cur.execute("CREATE TABLE hops(hop-id INT PRIMARY KEY AUTO_INCREMENT, \
                     hop-name VARCHAR(25), \
                     hop-aa INT, \
                     region-id INT)")

        # Initialize yeast table
        cur.execute("DROP TABLE IF EXISTS yeasts")
        cur.execute("CREATE TABLE yeasts(yeast-id INT PRIMARY KEY AUTO_INCREMENT, \
                     yeast-name VARCHAR(25), \
                     yeast-manufacturer VARCHAR(25))")

        #        cur.execute("INSERT INTO recipes(Name) VALUES('Hop Hammerish')")

def mysql_version():

    try:
        con = _mysql.connect('localhost', 'brew', 'brew', 'brew')
                
        con.query("SELECT VERSION()")
        result = con.use_result()
                            
        print "MySQL version: %s" % \
        result.fetch_row()[0]
                                                    
    except _mysql.Error, e:
      
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)

    finally:
        
        if con:
            con.close()

