#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    for l in f:
        left, right = sorted(list(map(int, l.split())))
        print(int((left + right) * (right - left + 1) / 2))
