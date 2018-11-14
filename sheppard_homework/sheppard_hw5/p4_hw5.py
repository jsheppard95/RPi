#!/usr/bin/env python3
# P4) Fourier Analysis
# p4_hw5.py
# Author: Jackson Sheppard
# 27Jul17 - Created

# This program reads in a data (.dat) file corresponding to Voltage vs. Time
# for a light source with periodic intensity and computes the power spectrum of 
# the signal to identify the fundamental frequency at which the light intensity
# varies

# modified from psd_spectrum.py

FTIME = 1       # function range in seconds
FS = 920         # samples per second
npts = FTIME*FS  # number of sample points
sampletime = 1/FS

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import psd
import matplotlib.mlab as mlb

t = np.arange(0, FTIME, sampletime)

# Read data file to get voltage array
v = np.zeros(npts, 'float')
infile = open('p3_hw5_voltdata.dat', 'r')
count = 0
for line in infile:
   v[count] = line
   count += 1
infile.close()

print("Creating power spectrum disrtibution...")
print("")

# Power Spectrum
ny, nx = psd(v, NFFT=npts, Fs=FS,detrend=mlb.detrend_mean, pad_to=16*npts)
f1, ax1 = plt.subplots()
ax1.plot(nx, ny)
ax1.set_xlim(0, 400)
ax1.set_xlabel('frequency, Hz')
ax1.set_ylabel('Intensity')
ax1.set_title('Intensity vs. frequency')
f1.show()
plt.savefig('p4_hw5_psdplot.eps')

# Find frequency with maximum intensity
max_index = np.argmax(ny)
freq_max = nx[max_index]

print("Resonant frequency:", freq_max, "Hz")
input("\nPress <Enter> to exit...\n")
