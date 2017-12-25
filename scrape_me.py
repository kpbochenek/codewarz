#!/usr/bin/env python3

import sys
import requests

url = sys.argv[1]
if not url.startswith('http'):
    url = 'http://' + url


r = requests.get(url)
print(r.text)
