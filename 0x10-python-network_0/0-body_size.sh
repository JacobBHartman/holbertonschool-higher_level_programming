#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL and displays
curl -I $1 | grep -e 'Content-Length' | cut -d: -f2 | cut -d' ' -f2
