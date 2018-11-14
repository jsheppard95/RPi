#!/usr/bin/env python3

# P8) Get Web Page with socket
# filename: p8_hw4.py
# author: Jackson Sheppard
# Last modified: 22Jul17

# Program that prints out for user when Phys 129 web page announcements
# were last updated using sockets.

import socket
import sys

port = 80

# Create socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get ip address:

# Connect to site:
s.connect(("http://www.physics.ucsb.edu/~phys129/lipman/", port))
s.sendall(b'GET / HTTP/1.0\n\n')
print(s.recv(4096))
s.close()
