#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API
to display your id
"""

if __name__ == "__main__":
    import sys
    import requests
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    resp = requests.get(url, auth=(username, password))
    print(resp.json().get('id'))
