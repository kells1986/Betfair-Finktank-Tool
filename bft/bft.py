#!/usr/bin/env python


import bfpy
import bfpy.bfclient as bfclient

import datetime
import operator
import sys


import simplejson as json
import urllib2
import getpass


user = raw_input('Betfair Username:')
passw = getpass.getpass('Betfair Password:')


bf = bfpy.BfClient()
try:
  bfresp  = bf.login(username=user, password=passw)
  print "logged in"
except bfpy.BfError, e:
  print "login error: %s" % str(e)
else:
  print bfresp

