#!/usr/bin/env python3
# P5) Heat Transfer
# b) Plot data with exponential curve fit
# p5b_hw5.py
# Author: Jackson Sheppard
# 28Jul17 - Created

# This program reads in the data file produced by the program p5a_hw5.py that
# contains the temperature as the sensor cools. The program fits an exponential
# function to this cooling period and plots the data alongside the curve. It 
# then determines the time constant of the exponential fit
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

ACQTIME = 120.0 # seconds of data acquisition
SPS = 4 # Sample rate
sinterval = 1.0/SPS
nsamples = int(ACQTIME*SPS)

# fit exponential curve to data:
def exp_func(x, a, k, b):
   return a*np.exp(-k*x)+b

# read in data from ouput file, add to new array
T = np.zeros(nsamples, 'float')
infile = open('p5_hw5_tempdata.dat', 'r')
index = 0
for line in infile:
   T[index] = float(line)
   index += 1
infile.close()

# Want to create exponential fit from cooling period only: find max temp
max_index = np.argmax(T)
T_fit = T[max_index:]

tpoints = np.linspace(0, ACQTIME, nsamples)
t_fit = tpoints[max_index:]

# Create exponential fit:
popt, pcov = curve_fit(exp_func, t_fit, T_fit, maxfev=10000)

# Plot data and exponential curve:
f2, ax2 = plt.subplots()
ax2.plot(tpoints, T, 'bx', label='data')

T_fit = exp_func(tpoints, *popt)
ax2.plot(tpoints, T_fit, 'r-', label='fit')
ax2.set_xlabel('time, seconds')
ax2.set_ylabel('Temperature, degrees Celcius')
ax2.set_title('Temperature vs. time, with best-fit')
ax2.legend()
f2.savefig('p5_hw5_tempbestfit.eps')
f2.show()

print("")
print("Fitted function: y = a*exp(-k*x) + b")
print("Best-fit parameters:")
print("a =", popt[0])
print("k =", popt[1])
print("b =", popt[2])

print("")
print("time constant of exponential: k =", popt[1], "s^-1")
input("\nPress <Enter> to exit...\n")

