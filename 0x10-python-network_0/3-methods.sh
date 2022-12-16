#!/bin/bash
# display methods accepted by a server
curl -s -X "OPTIONS" "$1" | grep "Allow" | cut -d ':' -f 2 | sed 's/ //'
