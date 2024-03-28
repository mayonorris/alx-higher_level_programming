#!/bin/bash
# This script sends a request to a URL passed as an argument and displays only the status code of the response
curl -s -o /tmp/status_code.tmp -w "%{http_code}" "$1"
