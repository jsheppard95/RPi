#!/usr/bin/env python3
# P5) Processor Temperature
# a)
import subprocess
import time

# Use subprocess module to read temperature file by running cat:
# Temperature file: /sys/class/thermal/thermal_zone0/temp

def getTemp():
  temp = subprocess.check_output(['cat', '/sys/class/thermal/thermal_zone0/temp'], universal_newlines=True) # Use cat command with temp file as argument
  # Convert temp from string to floating point and from millidegrees to degrees celcius
  temp_float = float(temp)
  temp_float = temp_float / 1000.0
  return temp_float

# We now have the processor temperature (in C) stored as a float in temp_float

# Function to print temperature once per second:
def periodic_print():
  while True:
    temp_float = getTemp()
    print('%.2f' % temp_float)
    time.sleep(1) # adds one second pause between iterations

# Calling both previous functions:
print('Processor Temperature (Degrees Celcius):')
print()
periodic_print() # Print processor temperature every 1 second

# b) Function to raise computer temperature
def raise_temp():
  while True:
    print('It\'s getting hotter')
# See file 'b' for implementation and analysis of this program
