#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    for l in f:
        left, right = map(int, l.split())
        prev, cur = 0, 1
        result = 0
        idx = 1
        while idx < right:
            if idx >= left and cur % 2 == 1:
                result += cur
            prev, cur = cur, prev + cur
            idx += 1
        print(result)

