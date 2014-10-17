#!/usr/bin/env python
# _*_ coding: utf_8 _*_

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
        cur.execute("CREATE TABLE recipes(batch_id INT PRIMARY KEY AUTO_INCREMENT, \
                     batch_name VARCHAR(25), \
                     grainbill_id INT, \
                     hopsch_id INT, \
                     dryhopsch_id INT, \
                     yeast_id INT, \
                     mash_id INT, \
                     gravity_id INT, \
                     refiner_id INT)")

        # Initialize grainbills table
        cur.execute("DROP TABLE IF EXISTS grainbills")
        cur.execute("CREATE TABLE grainbills(grainbill_id INT PRIMARY KEY AUTO_INCREMENT, \
                     grainbill_name VARCHAR(25))")

        # Initialize grains table
        cur.execute("DROP TABLE IF EXISTS grains")
        cur.execute("CREATE TABLE grains(grain_id INT PRIMARY KEY AUTO_INCREMENT, \
                     grain_name VARCHAR(25), \
                     region_id INT, \
                     grain_malter VARCHAR(25), \
                     grain_color VARCHAR(25), \
                     grain_region VARCHAR(25))")

        # Initialize hops table
        cur.execute("DROP TABLE IF EXISTS hops")
        cur.execute("CREATE TABLE hops(hop_id INT PRIMARY KEY AUTO_INCREMENT, \
                     hop_name VARCHAR(25), \
                     hop_aa INT, \
                     region_id INT)")

        # Initialize yeast table
        cur.execute("DROP TABLE IF EXISTS yeasts")
        cur.execute("CREATE TABLE yeasts(yeast_id INT PRIMARY KEY AUTO_INCREMENT, \
                     yeast_name VARCHAR(25), \
                     yeast_manufacturer VARCHAR(25))")

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


