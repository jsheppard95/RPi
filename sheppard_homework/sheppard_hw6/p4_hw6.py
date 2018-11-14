#!/usr/bin/env python3
# P4) Coin Toss Simulation
# p4_hw5.py
# Author: Jackson Sheppard
# 02Aug17 - Created

# This program contains a function simulating 100 coin tosses and returns the
# number of heads thrown.
# It then plots a histogram diplaying the result of 1000 function calls, and
# compares the distribution to a gaussian distribution

import numpy as np
import matplotlib.pyplot as plt

# a) Function to simulate 100 coin tosses:
# heads = 0, tails = 1
def coin_toss():
   """Function simulates 100 coin tosses: chooses either 0 or 1 randomly
   Returns number of heads through: number of 0's
   """
   count = 0
   for i in np.arange(100):
      flip = np.random.randint(0, 2)
      if flip == 0:
         count += 1
   return count

# b) Plot histogram displaying result of 1000 function calls
num_heads = np.zeros(1000) # entries correspond to function calls
for i in np.arange(1000):
   num_heads[i] = coin_toss()

f1, ax1 = plt.subplots()
heads_hist = ax1.hist(num_heads, 25, normed=True, label='(Number of Occurances)/1000')

# c) overlay a graph of the gaussian distibution the same mean and stddev
N = 100 # number of cointosses
p = 0.5 # probability of success
q = 1 - p
u = N*p # mean
sigma = np.sqrt(N*p*q) # standard deviation
# Gaussian: G(x) = (1/(sigma*sqrt(2*pi)))*exp(-(x-u)^2/(2*sigma^2))
xvals = np.linspace(0, N)
A = 1/(sigma*np.sqrt(2*np.pi))
b = 1/(2*sigma*sigma)
gauss = A*np.exp(-b*((xvals - u)**2))
curve = ax1.plot(xvals, gauss, 'r-', label='Gaussian Distribution')
ax1.set_xlabel("Number of Successes (Occurances of \"heads\") in 100 tosses")
ax1.set_title("Histogram for 100 Coin Tosses and Gaussian Curve")
ax1.legend()
f1.savefig('p4_hw6_histgauss.eps')
f1.show()
input("\nPress <Enter> to continue...\n")

