#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of the response
[[ $(curl -s -o /dev/null -w "%{http_code}" "$1") -eq 200 ]] && curl -s "$1"
