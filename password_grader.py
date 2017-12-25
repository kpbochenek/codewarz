#!/usr/bin/env python3

import sys
import string


with open(sys.argv[1], 'r') as f:
    for l in f:
        l = l[:-1]
        errors = 0

        lowerLetter = any(map(lambda x: x >= 'a' and x <= 'z', l))
        upperLetter = any(map(lambda x: x >= 'A' and x <= 'Z', l))
        number = any(map(lambda x: x >= '0' and x <= '9', l))
        punctuation = any(map(lambda x: x in string.punctuation, l))

        if not lowerLetter: errors += 1
        if not upperLetter: errors += 1
        if not number: errors += 1
        if not punctuation: errors += 1
        if len(l) > 20: errors += 1
        if len(l) < 8: errors += 1



        if not errors:
            print('Password: ({:02d}) {:<20}  Status: Passed all checks!'.format(len(l), l[:20]))
        else:
            if errors > 1:
                print('Password: ({:02d}) {:<20}  Status: Failed {} checks'.format(len(l), l[:20], errors))
            else:
                print('Password: ({:02d}) {:<20}  Status: Failed 1 check'.format(len(l), l[:20]))
