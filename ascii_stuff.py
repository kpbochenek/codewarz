#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    for l in f:
        nums = l.split()
        for n in nums:
            print(chr(int(n, base=16)), end='')
