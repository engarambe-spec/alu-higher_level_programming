#!/bin/bash
# sends a GET request to a URL and displays the body, only for a 200 status
[ "$(curl -s -o /tmp/1-body_response -w '%{http_code}' "$1")" = "200" ] && cat /tmp/1-body_response
