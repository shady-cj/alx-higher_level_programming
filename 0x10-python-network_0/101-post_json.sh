#!/bin/bash
# post a json data passed as a filename
curl -s -X POST -d "@$2" "$1"
