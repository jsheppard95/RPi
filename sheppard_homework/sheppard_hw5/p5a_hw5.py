#!/usr/bin/env python3
# P5) Heat Transfer
# a) Record temperature vs. time and plot raw data
# p5a_hw5.py
# Author: Jackson Sheppard
# 27Jul17 - Created
# 28Jul17 - Changed ACQTIME and plotted raw data

# This program acquires and saves temperature data at a rate of 4 samples per
# second as the MCP9808 sensor is heated and returns to room temperature.
# The program then produces an EPS plot of the raw data

import time
import Adafruit.MCP9808 as MCP9808
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

sensor = MCP9808()
sensor.begin()

ACQTIME = 120.0 # seconds of data acquisition
SPS = 4 # Sample rate: sample per second
sinterval = 1.0/SPS # Period: time length (in s) of one sample
nsamples = int(ACQTIME*SPS)

input('Press <Enter> to measure temperature for %s seconds...' % ACQTIME)
print()

# Initialize array to hold temperature:
T = np.zeros(nsamples, 'float')

t0 = time.perf_counter()

for i in range(nsamples):
   st = time.perf_counter() # current sample time
   temp = sensor.readTempC()
   T[i] = temp
   while (time.perf_counter() - st) <= sinterval:
      time.sleep(1.0e-7)

t = time.perf_counter() - t0 # should be close to ACQTIME

tpoints = np.arange(0, ACQTIME, sinterval)

# Create output file:
outfile = open('p5_hw5_tempdata.dat', 'w')
for i in T:
   outfile.write(str(i))
   outfile.write('\n')
outfile.close()

print('Time elapsed: %.9f.' % t)
print()

# Plot results
f1, ax1 = plt.subplots()
ax1.plot(tpoints, T, 'bo')
ax1.set_xlabel('time, seconds')
ax1.set_ylabel('Temperature, degrees Celcius')
ax1.set_title('Temperature vs. time')
f1.show()
f1.savefig('p5_hw5_tempplot.eps')
input("\nPress <Enter> to exit...\n")
