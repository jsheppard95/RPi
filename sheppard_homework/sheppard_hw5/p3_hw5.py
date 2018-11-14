#!/usr/bin/env python3
# P3) Acquire and Store Data
# p3_hw5.py
# Author: Jackson Sheppard
# 26Jul17 - Created

# This program acquires one second of voltage from the solar cell (Adafruit
# MCP9808) at a rates of 920 samples per second, plots the data, and stores the
# voltages in a text file with one voltage per line

# modified from fastadc.py

ACQTIME = 1.0 # seconds of data acquisition

SPS = 920 # Sample rate: samples per second

VRANGE = 6144 # full-scale Voltage range in mV

nsamples = int(ACQTIME*SPS)
sinterval = 1.0/SPS # Period: time length (in s) of one sample

import sys
import time
import numpy as np
import matplotlib.pyplot as plt

from Adafruit import ADS1x15

indata = np.zeros(nsamples,'float') # array to hold voltage data

print()
print('Initializing ADC...')
print()

#
# Default ADC IC is ADS1015
# Default address is 0x48 on the default I2C bus
#
adc = ADS1x15()

# First two arguments are the channels
# Third argument is the full-scale range in mV (default +/- 6144).
#    options: 256, 512, 1024, 2048, 4096, 6144.
#    Note: input should not exceed VDD + 0.3
# Fourth argument is samples per second (default 250).
#    options: 128, 250, 490, 920, 1600, 2400, 3300.
#
adc.startContinuousDifferentialConversion(2, 3, pga=VRANGE, sps=SPS)

input('Press <Enter> to start %.1f s data acquisition...' % ACQTIME)
print()

t0 = time.perf_counter()

for i in range(nsamples):
   st = time.perf_counter() # current sample time
   indata[i] = 0.001*adc.getLastConversionResults() # .001 converts mV to V
   while (time.perf_counter() - st) <= sinterval:
      time.sleep(1.0e-7)

t = time.perf_counter() - t0

adc.stopContinuousConversion()

xpoints = np.arange(0, ACQTIME, sinterval)

# Create output file:
outfile = open('p3_hw5_voltdata.dat', 'w')
#outfile = open('p4_hw5_voltdata.dat', 'w') # used for problem 4
for i in indata:
   outfile.write(str(i))
   outfile.write('\n')
outfile.close()

print('Time elapsed: %.9f.' % t)
print()

f1, ax1 = plt.subplots()
ax1.plot(xpoints, indata, 'b-')
ax1.set_title('Voltage vs. Time')
ax1.set_xlabel('Time, seconds')
ax1.set_ylabel('Voltage, volts')
f1.show()
f1.savefig('p3_hw5_voltfig.eps')
input("\nPress <Enter> to exit...\n")


