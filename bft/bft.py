#!/usr/bin/env python


import bfpy
import bfpy.bfclient as bfclient

import datetime
import operator
import sys


import simplejson as json
import urllib2


bf = bfpy.BfClient()
try:
  bfresp  = bf.login(username='kelbet86', password='cahoots1')
  print "logged in"
except bfpy.BfError, e:
  print "login error: %s" % str(e)
else:
  print bfresp

