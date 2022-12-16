#!/usr/bin/python3
"""
a Python script that fetches
https://alx-intranet.hbtn.io/status using requests
"""

if __name__ == "__main__":
    import requests

    res = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print(f"    - type: {type(res.text)}")
    print(f"    - content: {res.text}")
