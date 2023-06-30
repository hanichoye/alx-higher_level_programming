#!/usr/bin/python3
"""script which displays the value of the X-Request-Id variable found in
the header of the response.
"""

import requests
from sys import argv

if __name__ == "__main__":
    print(requests.get(argv[1]).headers.get("X-Request-Id"))
