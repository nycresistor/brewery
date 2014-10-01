#!/usr/bin/env python
# -*- coding: utf-8 -*-

# a license should be at the top of all python source code

import argparse

from api import debug
from api import funcs
from common import db

from cgi import parse_qs

from wsgiref.simple_server import make_server

# parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--wsgiport', help='port of wsgi server', default='8080')
parser.add_argument('-d', '--debug', action="count",
                    help='turn on debugging output')
args = parser.parse_args()

# pull in arguments to vars force type
wsgiport = int(args.wsgiport)
status_file = str(args.statuspath)

# initialize database
conn = db.db_init(status_file)

def REST_api(environ, start_response):
    
    # get arguments
    parameters = parse_qs(environ.get('QUERY_STRING', ''))

    # query functions 
    wdict = funcs.query(conn, parameters)

    # format response from wdict
    status = wdict['status']
    headers = wdict['headers']
    status_string = wdict['status_string']
    start_response(status, headers)

    return [status_string]

if (args.debug == 1):
    REST_api = debug.debugger(REST_api)
    print "Debugging On."

httpd = make_server('', wsgiport, REST_api)
print "Serving on port %s..." % wsgiport

# Serve until process is killed
httpd.serve_forever()

