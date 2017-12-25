#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    for l in f:
        left, right = sorted(map(float, l.split()))
        current = 1
        while current <= right:
            if int(current) == current and (int(current) / left).is_integer():
                print(int(current))
            current += 1
        print()

