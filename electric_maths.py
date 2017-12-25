#!/usr/bin/env python3

import sys
import socket

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
task = s.recv(1024).decode("utf-8").splitlines()[1]

if 'subtract' in task:
    task = task.split()
    a, b = float(task[1]), float(task[3][:-1])
    answer = b - a
elif 'multiply' in task:
    task = task.split()
    a, b = float(task[1]), float(task[3][:-1])
    answer = a * b
elif 'add' in task:
    task = task.split()
    a, b = float(task[1]), float(task[3][:-1])
    answer = a + b
elif 'divide' in task:
    task = task.split()
    a, b = float(task[1]), float(task[3][:-1])
    answer = a / b

if int(answer) == answer:
    answer = str(int(answer))
else:
    answer = str(round(answer, 8))

s.send(bytes(answer+"\n", encoding='utf-8'))

print(s.recv(1024).decode("utf-8"), end='')
