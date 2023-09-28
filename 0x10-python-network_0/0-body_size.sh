#!/bin/bash
# Display size of body of response; Usage: ./0-body_size.sh 0.0.0.0:5000

URL="$1"
headers_file=$(mktemp)
curl -sI "$URL" -o "$headers_file"
response_size=$(grep 'Content-Length:' "$headers_file" | cut -f2 -d' ')
echo ${response_size}