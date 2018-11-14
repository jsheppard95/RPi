#!/usr/bin/env python3
# P6) Polynomial Fits
# p6_hw5.py
# Author: Jackson Sheppard
# 29Jul17 - Created

# This program generates a user-specified number N of random points in the xy
# plane, with x and y both running from 0-100. The program finds fits to
# the data using polynomials of degree 1, N - 3, and N - 1. 

import numpy as np
import random
import matplotlib.pyplot as plt

N = int(input("Enter number of points to draw: "))
while N >= 100:
   N = int(input("Too many points, please choose less than 100 points: "))

# Create random data points:
xdata = np.random.random_sample([N]) # generates N random points
ydata = np.random.random_sample([N])
xdata *= 100 # points 0-100 instead of 0-1
ydata *= 100

# Plot data:
f1, ax1 = plt.subplots()
ax1.plot(xdata, ydata,'bo', label='data')
ax1.set_xlabel('x')
ax1.set_ylabel('y')

# Create polynomial fits:
poly_1 = np.polyfit(xdata, ydata, 1)
p1 = np.poly1d(poly_1)
poly_N_3 = np.polyfit(xdata, ydata, N-3)
pN_3 = np.poly1d(poly_N_3)
poly_N_1 = np.polyfit(xdata, ydata, N-1)
pN_1 = np.poly1d(poly_N_1)
x_fit = np.linspace(0, 100, 100)

ax1.plot(x_fit, p1(x_fit), 'r-', label='fit degree 1')
ax1.plot(x_fit, pN_3(x_fit), 'g-', label='fit degree N-3')
ax1.plot(x_fit, pN_1(x_fit), 'y-', label='fit degree N-1')

ax1.set_xlim(0, 100)
ax1.set_ylim(0, 100)
ax1.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
ax1.set_title('N=%d random points and polynomial fits' % N)
f1.show()
f1.savefig('p6_hw5_polyfits.eps')
input("\nPress <Enter> to exit...\n")

