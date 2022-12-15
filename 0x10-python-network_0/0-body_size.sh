#!/bin/bash
# Getting the size of the body from curl result

curl -s "$1" | wc -c
