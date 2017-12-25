#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    for l in f:
        rev = "".join(reversed(l))
        print(l.strip() == rev.strip())
