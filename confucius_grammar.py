#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    for l in f:
        capitalize = True
        out = []
        for w in l.split():
            if capitalize or w.lower() == 'i':
                out.append(w.capitalize())
            else:
                out.append(w.lower())
            capitalize = False
            if w.endswith('.'):
                capitalize = True
        print(" ".join(out))
