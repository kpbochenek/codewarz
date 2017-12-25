#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    for l in f:
        left, right = list(map(int, l.split()))
        result = []
        current = left
        while current <= right:
            if current % 7 == 0 and current % 5 != 0:
                result.append(current)
            current += 1
        print(",".join(map(str, result)))
