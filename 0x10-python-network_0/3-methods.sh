#!/bin/bash
# takes in a url and displays all HTTPS methods
curl -sD - 0.0.0.0:5000/route_4 | grep -e "Allow:" | cut -c8-
