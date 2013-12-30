#!/usr/bin/env python


import bfpy
import bfpy.bfclient as bfclient

import datetime
import operator
import sys


import simplejson as json
import urllib2
import getpass

def log_in():
	user = raw_input('Betfair Username:')
	passw = getpass.getpass('Betfair Password:')

	bf = bfpy.BfClient()
	try:
		bfresp  = bf.login(username=user, password=passw)
	except bfpy.BfError, e:
		print "login error"
	else:
  		print "Logged In"

	return bf

bf = log_in()

