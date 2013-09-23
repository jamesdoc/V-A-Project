#!/usr/bin/python

import urllib2, json

#base_url = 'http://www.vam.ac.uk/api/json/museumobject/search?';
base_url = 'http://www.vam.ac.uk/api/json/museumobject/search?materialsearch=gold&limit=10'

response = urllib2.urlopen(base_url)

json_object = json.loads(response.read())

print '<table>';\
print '<thead><tr><th>Name</th><th>Location</th></tr></thead>';\

for item in json_object['records']: 
    
    print '<tr>';\
    
    if item['fields']['title']:
        print '<td>' + item['fields']['title'] + ' - ' + item['fields']['object'] + '</td>';\
        
    else:
        print '<td>' + item['fields']['object'] + '</td>';\
    
    print '<td>' + item['fields']['location'] + '</td>';\
    print '</tr>';\
    
print '</table>';\