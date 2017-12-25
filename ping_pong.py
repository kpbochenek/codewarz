#!/usr/bin/env python3

import sys
import requests

ping = sys.argv[1]
pong = sys.argv[2]
word = sys.argv[3]

if not ping.startswith('http'):
    ping = 'http://' + ping
if not pong.startswith('http'):
    pong = 'http://' + pong


while True:
    r = requests.post(ping, data={'food': word})
    answer = r.text
    if 'serving' not in answer:
        print(answer, end='')
        break

    word = answer.split()[2]
    ping, pong = pong, ping
