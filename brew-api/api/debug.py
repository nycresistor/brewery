#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exc_info
from traceback import format_tb

class debugger(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        app = None
        try:
            app = self.app(environ, start_response)
            for item in app:
                yield item
        except:
            e_type, e_value, tb = exc_info()
            traceback = ['Traceback (most recent call last):']
            traceback += format_tb(tb)
            traceback.append('%s: %s' % (e_type.__name__, e_value))
            try:
                start_response('500 INTERNAL SERVER ERROR', [
                               ('Content-Type', 'text/plain')])
            except:
                pass
            yield '\n'.join(traceback)

        if hasattr(app, 'close'):
            app.close()
