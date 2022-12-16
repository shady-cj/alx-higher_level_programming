#!/bin/bash
# display methods accepted by a server
curl -sL -w "%{http_code}" "$1" 
