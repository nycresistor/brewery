#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import re
import sqlite3
import sys
import time
import traceback

from dpkg import parse
from dpkg import poll

def db_init(status_file):
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

def db_query(conn, query):
    db_resp = conn.execute(query).fetchall()
    return db_resp

def db_create(conn):
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
