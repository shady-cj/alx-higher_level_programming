#!/usr/bin/python3
"""
A python script that takes in a URL and sends
a request to the URL and displays the value
of the X-Request-Id variable found in the
header response
"""
import urllib.request
import sys

url = sys.argv[1]
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as res:
    print(res.headers.get('X-Request-Id'))
