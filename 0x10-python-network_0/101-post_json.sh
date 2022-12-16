#!/bin/bash
# post a json data passed as a filename
curl -sL -X POST -H "Content-Type: application/json" -d "@$2" "$1"
