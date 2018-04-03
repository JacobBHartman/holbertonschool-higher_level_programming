#!/bin/bash
# takes in a url and displays all HTTPS methods
curl -sD - $1 | grep -e "Allow:" | cut -c8-
