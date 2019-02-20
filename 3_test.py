import json
import urllib2

data = {"registers": [1, 2, 3, 4, 5],
        "values": [1, 2, 3, 4, 5]}
req = urllib2.Request('http://127.0.0.1:5000/write')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
print(response)

data = {"registers": [1, 2, 3, 4, 5]}
req = urllib2.Request('http://127.0.0.1:5000/read')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
print(response)
