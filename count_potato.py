#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    for l in f:
        left, right = l.split()
        left, right = int(left)-1, right.split(',')
        idx = (left+1) % len(right)
        while idx != left:
            if right[idx] > right[left]:
                print(right[idx])
                break
            idx = (idx + 1) % len(right)
        else:
            print()

