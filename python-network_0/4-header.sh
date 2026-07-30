#!/bin/bash
# sends a GET request with a custom X-HolbertonSchool-User-Id header
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
