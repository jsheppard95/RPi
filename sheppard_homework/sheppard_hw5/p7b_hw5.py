#!/usr/bin/env python3
# P7) Monte Carlo Circle
# b) Plotting fraction error in Monte Carlo pi approximation vs. N
# p7b_hw5.py
# Author: Jackson Sheppard
# 29Jul17Created

# This program plots the fractional error in the determined value of pi (found
# using function within p7a_hw5.py called monte_carlo_pi(N)) vs. N and outputs
# the plot as an .eps file

import matplotlib.pyplot as plt
from p7a_hw5 import monte_carlo_pi
import numpy as np

NPTS = 1000

print("Creating plot...")
print("")

# fractional error (estimate - actual)/actual
# low fractional error => estimate very accurate
Nvals = np.arange(1, NPTS+1)
err_vals = np.zeros(NPTS, 'float')
for i in range(len(Nvals)):
   est = monte_carlo_pi(Nvals[i])
   err = abs(est - np.pi)/np.pi
   err_vals[i] = err

# Plot error vs. N:
f1, ax1 = plt.subplots()
ax1.plot(Nvals, err_vals, 'bo')
ax1.set_xlabel('N')
ax1.set_ylabel('fractional error')
ax1.set_title('fractional error: (actual - estimate)/actual vs. N')
f1.show()
f1.savefig('p7_hw5_errorplot.eps')
input("\nPress <Enter> to exit...\n")
