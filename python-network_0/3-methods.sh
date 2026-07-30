#!/bin/bash
# displays all HTTP methods a server will accept for the given URL
curl -s -X OPTIONS -i "$1" | grep -i "^Allow:" | cut -d' ' -f2- | tr -d '\r'
