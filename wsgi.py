#!/usr/bin/env python
"""Bottle Hello world"""

import bottle

def hello():
    """Return 'hello world' string"""
    return '<!DOCTYPE html>\n<title>Hello world</title>\n<p>Hello world</p>\n'

bottle.route('/', 'GET', hello)

application = bottle.default_app() # pylint: disable-msg=C0103
if __name__ == '__main__':
    bottle.run(application, host='0.0.0.0', port=8080)
