#!/usr/bin/env python3
# P7) Monte Carlo Circle
# a) Approximation of pi
# p7a_hw5.py
# Author: Jackson Sheppard
# 29Jul17 - Created

# This program generates a user-specified number N of uniformly distributed
# random points in the xy plane with x and y both running from 0-2. 
# By counting the number of points within the sircle of radius 1 centered at
# (1,1), the program estimates the value of pi

import numpy as np
import random

def monte_carlo_pi(N):
   """This function takes in N data points and returns an approximation for pi
   by the monte carlo circle
   """
   # create random data points:
   coordinates = np.random.random_sample([N,2]) # generates N random (x,y) points from 0-1
   coordinates *= 2 # scale points from 0-2 instead of 0-1
   # coordinates = N by 2 array standing for N (x,y) coordinate pairs
   # Iterate through (x,y) points to determine if point is in circle
   # point is in circle if (x,y) satisfies: (x-1)^2 + (y-1)^2 <= 1

   N_circle = 0
   for point in coordinates:
      if ( ((point[0] - 1)**2) + ((point[1] - 1)**2) ) <= 1:
         N_circle += 1

   # Now know: N_circle/N = pi/4 -> pi = 4*N_circle/N
   mc_pi = 4*N_circle/N # estimate of pi
   return mc_pi

if __name__ == "__main__":
   # Only excutes if program called in terminal
   # Allows one to import monte_carlo_pi function only
   N = int(input("Enter number of points to plot: "))
   print("Estimated area of circle/value of pi:", monte_carlo_pi(N))

