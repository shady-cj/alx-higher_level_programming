#!/bin/bash
# display methods accepted by a server
curl -s -X "OPTIONS" "$1"
