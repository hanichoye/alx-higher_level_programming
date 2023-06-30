#!/bin/bash
# The script that displays the body of the response and sends a DELETE request to the URL passed as the first argument
curl -s "$1" -X DELETE
