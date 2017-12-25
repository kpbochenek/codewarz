#!/usr/bin/env python3

import sys
import socket

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
for i in range(300000):
    s.send(bytes(str(i) + "\n", 'utf-8'))
    resp = s.recv(1024).decode("utf-8")
    if not "Pick a number" in resp:
        print(resp, end='')
        break
