#!/bin/bash
# This script takes a URL, sends a request, and displays the size of the response body in bytes
curl -sI "$1" | grep -i "content-length" | awk '{print $2}'
