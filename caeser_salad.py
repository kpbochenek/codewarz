#!/usr/bin/env python3

import sys


def dec(c, i):
    if c >= 'a' and c <= 'z':
        next = (ord(c) - ord('a') - i + 26) % 26
        return chr(ord('a') + next)
    return c


def decode(w):
    global idx
    idx += 1
    return "".join([dec(p, idx) for p in w])


with open(sys.argv[1], 'r') as f:
    for l in f:
        out = []
        idx = -1
        for w in l.split():
            out.append(decode(w))
        print(" ".join(out))
