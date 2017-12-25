#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    for l in f:
        elems = l.split()
        print(sum(map(int, elems)) + len(elems))
