#!/usr/bin/python3
"""
A program that lists 10 commits
(from the most recent to oldest) of the
repository “rails” by the user “rails”
You must use the GitHub API,
here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""


if __name__ == "__main__":
    import requests
    import sys

    owner_name = sys.argv[1]
    repo_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}\
/{repo_name}/commits"
    resp = requests.get(url)
    data = resp.json()

    for commit in data[:10]:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")
