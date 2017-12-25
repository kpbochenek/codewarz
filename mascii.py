#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    for l in f:
        for c in l.split(' '):
            if c.startswith('0x'):
                print(chr(int(c, base=16)), end='')
            elif c.startswith('0b'):
                print(chr(int(c, base=2)), end='')
            elif c.startswith('0'):
                print(chr(int(c, base=8)), end='')
            else:
                print(chr(int(c)), end='')


