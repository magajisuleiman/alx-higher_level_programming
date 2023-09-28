#!/bin/bash
# Display size of body of response; Usage: ./0-body_size.sh 0.0.0.0:5000

headers_file=$(mktemp)
curl -sI "$1" -o "$headers_file" | grep 'Content-Length:' "$headers_file" | cut -f2 -d' '