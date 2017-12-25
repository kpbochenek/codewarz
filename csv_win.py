#!/usr/bin/env python3

import sys
import csv

with open(sys.argv[1], 'r', newline='') as f:
    print(sum([sum(map(float, row)) for row in csv.reader(f)]))

