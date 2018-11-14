#!/usr/bin/env python3

# P10) Time Server
# filename: p10_hw4.py
# author: Jackson Sheppard
# Last modified: 22Jul17

# Program serves current time in human-readable format when a connect is
# established to TCP port 55555 on RPi

import socket
import time
import tempfile
import os

def bind_port(prt):
   """Create socket and bind to port prt.
   """

   host = ''  # bind to all available interfaces

   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # reuse port
   s.bind((host, prt))
   s.listen(1)

   return(s)

# bind to port 55555
thesocket = bind_port(55555)

# Get current local time
current_time = time.asctime() # connection time

# Write connection time to output file
time_file = open('time_file.txt', 'w')
time_file.write('Local date and time:\n')
time_file.write(current_time)
time_file.close()

# Read time_file to send through socket
with open('time_file.txt', 'rb') as datafile:
   out_time = datafile.read()

outdata = b'\n\nWe Have a connection!\n\n'

connection, peer = thesocket.accept()
connection.sendall(outdata) # Send connection message
connection.sendall(out_time) # Send connection time
connection.shutdown(socket.SHUT_RDWR)
connection.close() # close connection

os.remove('time_file.txt') # remove file containing connection time
