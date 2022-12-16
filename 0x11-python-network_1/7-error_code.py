#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response.
"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]

    resp = requests.get(url)
    s_code = resp.status_code
    if s_code >= 400:
        print("Error code:", s_code)
    else:
        print(resp.text)
