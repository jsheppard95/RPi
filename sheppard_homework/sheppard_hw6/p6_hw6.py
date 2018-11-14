#!/usr/bin/env python3
# P6) Numerical Integration
# p6_hw6.py
# Author: Jackson Sheppard
# 04Aug17 - Created
# 04Aug17 - Added Error plots vs. N

# This program computes integral(-inf, inf){exp(-x^2)dx} by two numerical
# methods: adding the areas of rectangle and using a Monte Carlo simulation

# Note: at x = +/- 10, y = exp(-x^2) ~ 10^-44 and continues decreasing moving
# toward +/- infinity. We can thus set our limits of integration as +/- 10

import numpy as np
import matplotlib.pyplot as plt

N_MAX = 1000 # Max number of rectangles or random points for plotting error
LOW_LIM = -5.0
UP_LIM = 5.0
ACTUAL_VALUE = np.sqrt(np.pi)

print('Finding Integral over entire x axis (-infity, infinity) of:')
print('y = exp(-x^2)')
print('Known value: sqrt(pi) = %.9f' % ACTUAL_VALUE)

# a) Adding the areas of rectangle

def rect_int(N, low_lim, up_lim):
   """approximates integral by adding rectangles
   N: number of rectangles, low_lim: lower limit, up_lim: upper limit
   returns: approximate integral of Exp(-x^2) from low_lim to up_lim
   """
   xvals = np.linspace(low_lim, up_lim, N)
   yvals = np.exp(-(xvals**2))
   delta = (up_lim - low_lim)/N
   integral = (yvals*delta).sum()
   return integral

print('')
print('N = 100000')
est_rect = rect_int(100000, LOW_LIM, UP_LIM)
print('rectangle method:', est_rect)
print('fractional error: %.9f' % (abs(est_rect - ACTUAL_VALUE)/ACTUAL_VALUE))

def mc_int(N, low_lim, up_lim):
   """approximates integral by monte carlo simulation
   N: number of random points, low_lim: lower limit, up_lim: upper limit
   returns: approximate integral of Exp(-x^2) from low_lim to up_lim
   """
   xpts = np.random.uniform(low_lim, up_lim, N)
   ypts = np.random.random(N)
   coords = np.column_stack((xpts, ypts)) # Now have N random (x,y) coordinates
   # Iterate through each (x,y) point and determine if it falls with the
   # gaussian curve
   # random point (x,y) within curve f(x) if y <= f(x), else: not inside curve
   N_gauss = 0
   for point in coords:
      if point[1] <= (np.exp(-(point[0]**2))):
         N_gauss += 1
   # Now know: N_gauss/N = A_gauss/A_tot
   # A_tot = rectangle: width = up_lim - low_lim, height = 1
   # A_tot = up_lim - low_lim
   # A_gauss = (N_gauss/N)*A_tot
   integral = (N_gauss/N)*(up_lim - low_lim)
   return integral

est_mc = mc_int(100000,LOW_LIM,UP_LIM)
print('Monte Carlo Simulation:', est_mc)
print('fractional error: %.9f' % (abs(est_mc - ACTUAL_VALUE)/ACTUAL_VALUE))
print('')

# Produce plot for each method of fractional error (from known value sqrt(pi))
# versus N (number of rectangles or random points)
Nvals = np.arange(1, N_MAX + 1)
rect_err = np.zeros(N_MAX, 'float')
mc_err = np.zeros(N_MAX, 'float')

print("Getting Fractional Error vs N...")

for N in Nvals:
   est_rect = rect_int(N, LOW_LIM, UP_LIM)
   rect_err[N-1] = abs(est_rect - ACTUAL_VALUE)/np.sqrt(np.pi)
   est_mc = mc_int(N, LOW_LIM, UP_LIM)
   mc_err[N-1] = abs(est_mc - ACTUAL_VALUE)/np.sqrt(np.pi)
print('done')

# Plot error in rectangle method:
f1, ax1 = plt.subplots()
ax1.plot(Nvals, rect_err, 'bo')
ax1.set_xlabel('Number of Rectangles, N')
ax1.set_ylabel('fractional error = |actual - estimate|/actual')
ax1.set_title('Fractional Error in Rectangle Method vs. N')
f1.savefig('p6_hw6_rect_errorplot.eps')
f1.show()

# Plot error in Monte Carlo Simulation:
f2, ax2 = plt.subplots()
ax2.plot(Nvals, mc_err, 'ro')
ax2.set_xlabel('Number of Random Points, N')
ax2.set_ylabel('fractional error = |actual - estimate|/actual')
ax2.set_title('Fractional Error in Monte Carlo Simulation vs. N')
f2.savefig('p6_hw6_mc_errorplot.eps')
f2.show()

input("\nPress <Enter> to exit...\n")
