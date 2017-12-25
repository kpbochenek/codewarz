#!/usr/bin/env python3

import sys
# from collections import defaultdict

tens = [0 for i in range(100000)]
max_val = 0

with open(sys.argv[1], 'r') as f:
    for l in f:
        val = int(l)
        tens[val // 10] += 1
        max_val = max(max_val, val // 10)

for i in range(max_val+1):
    print(tens[i], end='')

