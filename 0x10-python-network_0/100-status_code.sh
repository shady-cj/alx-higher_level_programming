#!/bin/bash
# display methods accepted by a server
curl -sL -o /dev/null -w "%{http_code}" "$1" 
