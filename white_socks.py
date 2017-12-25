#!/usr/bin/env python3

import sys
import socket

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print(s.recv(1024).decode("utf-8"))
