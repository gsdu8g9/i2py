#!/usr/bin/env python
# coding: utf-8
#
# demo.py - I2PControl demo, show basic statistics.
# License: public domain / unlicense
#
# This is the same as running `python -m i2pcontrol` from a command line.

import i2py.control

a = i2py.control.I2PControl()
print(a.get_network_settings())
vals = a.get_router_info()
print(''.join([
    'You are running i2p version ', str(vals['i2p.router.version']), '. ',
    'It has been up for ', str(vals['i2p.router.uptime']), 'ms. ',
    'Your router knows ', str(vals['i2p.router.netdb.knownpeers']),' peers.'
    ]))
