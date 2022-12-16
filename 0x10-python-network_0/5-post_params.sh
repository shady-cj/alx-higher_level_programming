#!/bin/bash
# display methods accepted by a server
curl -s -X "POST" -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
