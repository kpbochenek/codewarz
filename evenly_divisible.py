#!/usr/bin/env python3

# TODO: WRONG SOLUTION !!!!!!!!
import sys

with open(sys.argv[1], 'r') as f:
    for l in f:
        left, right = sorted(map(float, l.split()))
        current = left
        while current <= right:
            if int(current) == current:
                print(int(current))
            current += left
        print()

