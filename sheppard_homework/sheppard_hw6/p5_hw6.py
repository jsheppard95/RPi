#!/usr/bin/env python3
# P5) Counting Simulation
# p5_hw6.py
# Author: Jackson Sheppard
# 03Aug17 - Created

# This program contains a function which simulated photon counting for 1000
# one millisecond intervals. Probability of detection in each interval is
# .0002, function returns number of detections
# The program then plots a histogram of 1000 function calls, and overlays the
# plot with a graph of the Poisson distribution

import numpy as np
import matplotlib.pyplot as plt

# a) Function that simulates photon detection:
# prob of detection = .002
def photon_detection():
   """Function simulates 1000 one millisecond intervals in which the
   probability of detetction is .002. Function returns number of
   detections
   """
   count = 0
   for i in range(1000):
      check = np.random.random() # returns random float between 0 and 1
      if check <= .002: # photon detected
         count += 1
   return count

# b) Plot histogram displaying result of 1000 function calls:
num_detects = np.zeros(1000) # entries = number of detections for each call
for i in np.arange(1000):
   num_detects[i] = photon_detection()

f1, ax1 = plt.subplots()
detect_hist = ax1.hist(num_detects, 10, normed=True, label='(Number of Occurances)/1000')

# c) overlay plot of Poisson distribution:
# P(n) = (u^n)*e^(-u)/n!
# n = total number of successes, u = Np = mean (n = num trials)
# sigma = sqrt(u) = stddev

N = 1000
p = .002
u = N*p
sigma = np.sqrt(u)
nvals = np.arange(15)
Pvals = np.zeros(15)
for n in nvals:
   Pvals[n] = (u**n)*np.exp(-n)/np.math.factorial(n)
curve = ax1.step(nvals, Pvals, 'r-', label='Poisson Distribution')

ax1.set_xlabel("Number of Sucesses (photon detections), n")
ax1.set_title("Histogram for Photon detections in 1000 intervals and Poisson Distribution")
ax1.legend()
f1.savefig('p5_hw6_histpoiss.eps')
f1.show()
input("\nPress <Enter> to continue...")
