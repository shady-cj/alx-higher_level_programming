#!/usr/bin/python3
"""
a Python script that takes in a letter
and sends a POST request to
http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    data = {"q": q}
    url = "http://0.0.0.0:5000/search_user"
    resp = requests.post(url, data=data)

    try:
        result = resp.json()
        if len(result):
            print(f"[{result.get('id')}] {result.get('name')}")
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
