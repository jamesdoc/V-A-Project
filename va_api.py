#!/usr/bin/python

import urllib2, json

#base_url = 'http://www.vam.ac.uk/api/json/museumobject/search?';
base_url = 'http://www.vam.ac.uk/api/json/museumobject/search?materialsearch=gold'

response = urllib2.urlopen(base_url)

json_object = json.loads(response.read())

for item in json_object['records']:   
        print item;\
        print ;\