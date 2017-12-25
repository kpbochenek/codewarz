#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    for l in f:
        print(sum(map(lambda x: int(x, base=2), l.split())))
