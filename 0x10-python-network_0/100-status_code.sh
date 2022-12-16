#!/bin/bash
# displays the status code by d server
curl -sL -o /dev/null -w "%{http_code}" "$1" 
