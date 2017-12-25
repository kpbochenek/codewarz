#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    for l in f:
        words = l.split()
        add_next = True
        for w in words:
            if add_next:
                print(w, end=' ')
            add_next = False
            if w.endswith('.'):
                add_next = True
