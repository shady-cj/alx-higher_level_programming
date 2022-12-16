#!/bin/bash
# display methods accepted by a server
curl -I "$1" | grep "Allow" | cut -d ' ' -f 2
