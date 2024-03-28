#!/bin/bash
# This script sends a JSON POST request to the URL with the contents of a file as the body, and displays the body of the response.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
