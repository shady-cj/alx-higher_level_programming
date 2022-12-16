#!/usr/bin/python3
"""
A python module that uses urllib to make request
to https://alx-intranet.hbtn.io/status
"""
import urllib.request

req = urllib.request.Request('https://alx-\
intranet.hbtn.io/status')

with urllib.request.urlopen(req) as res:
    con = res.read()
    typ = type(con)
    utf8 = con.decode('utf-8')

    print("Body response:")
    print(f"    - type: {typ}")
    print(f"    - content: {con}")
    print(f"    - utf8 content: {utf8}")
