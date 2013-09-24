#!/usr/bin/env python

import requests

try:
	r = requests.get('https://github.com/timeline.json', timeout=5)
	
	print r.text
except requests.exceptions.RequestException, e:
       print 'error'