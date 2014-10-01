#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _mysql
import json
import MySQLdb as mdb
import os
import re
import sqlite3
import sys
import time
import traceback

def mysql_init():
    con = mdb.connect('localhost', 'brew', 'brew', 'brew');

    with con:
    
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS recipes")
        cur.execute("CREATE TABLE recipes(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 Name VARCHAR(25))")
        cur.execute("INSERT INTO recipes(Name) VALUES('Hop Hammerish')")
        cur.execute("INSERT INTO recipes(Name) VALUES('Hop Bomber')")
        cur.execute("INSERT INTO recipes(Name) VALUES('Anthony Janszoon Van Salle Porter')")
        cur.execute("INSERT INTO recipes(Name) VALUES('Beer 2')")       

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

def sqlite_init(status_file):
    # poll status file
    status_obj = poll.poll(status_file)
    
    # initialize sqlite3
    conn = sqlite3.connect(":memory:")
    db_create(conn)

    # parse status fileobject, load into database
    db_status_load(conn, status_obj)

    # kill that big string obj
    del status_obj

    # return ready database handle
    return conn

def sqlite_query(conn, query):
    db_resp = conn.execute(query).fetchall()
    return db_resp

def sqlite_create(conn):
    c = conn.cursor()

    c.execute('PRAGMA temp_store=MEMORY;')
    c.execute('PRAGMA journal_mode=MEMORY;')

    # tables, and a dependency index 
    c.execute('create table if not exists brews (brewid integer primary key autoincrement, brewname text, brewdesc blob);')
    c.execute('create table if not exists brewers (brewerid int, brewername text);')
    c.execute('create table if not exists kegs (kegid int, kegsize int, kegtype int);')
    c.execute('create table if not exists kegtypes (ktypeid int, ktypename text);')
    c.execute('create table if not exists carboys(carboyid int, carboysize int, carboytype int);')
    c.execute('create table if not exists carboytypes(carboytypeid, carboytypename text);')
    c.execute('create table if not exists grains (grainid int, grainname text);')
    c.execute('create table if not exists hops (hopsid int, hopsname text);')
    c.execute('create table if not exists refiners (refinerid int, refinername text);')
    c.execute('create table if not exists additives (additiveid int, additivename text);')
    conn.commit()

    return 0

def db_add_kegtype(conn, kegtypename):
    return 0

def db_add_carboytype(conn, carboytypename):
    return 0

def db_add_brew(conn, brewname, brewdesc, recipe):
    return 0

def db_add_brewer(conn, brewername):
    return 0

def db_add_grain(conn, grainname):
    return 0

def db_add_hops(conn, hopsname):
    return 0

def db_add_refiner(conn, refinername):
    return 0

def db_add_additive(conn, additivename):
    return 0
