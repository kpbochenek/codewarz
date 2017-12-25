#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    for l in f:
        result = map(lambda x: chr(int(x)), l.split())
        print("".join(result))
