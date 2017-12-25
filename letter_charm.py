#!/usr/bin/env python3

import sys

def fix(w):
    if len(w) >= 3:
        return w[1:3] + w[0] + w[3:]
    return w

with open(sys.argv[1], 'r') as f:
    for l in f:
        print(" ".join(map(fix, l.split())))
