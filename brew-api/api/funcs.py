#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from cgi import escape
from common import db

def query(conn, parameters):

    wdict = {}
    wdict['status'] = '200 OK'
    wdict['headers'] = [('Content-type', 'text/html')]
    if 'describe' in parameters:
        param = escape(parameters['describe'][0])
        status_string = package_describe(conn, param)
        status_string += package_depends(conn, param)
        status_string += package_dependees(conn, param)
        wdict['status_string'] = status_string
    else:
        status_string = package_list(conn)
        wdict['status_string'] = status_string
    return wdict
