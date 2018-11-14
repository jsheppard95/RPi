#!/usr/bin/env python3

# P11) Plot Trig Functions
# filename: p11_hw4.py
# author: Jackson Sheppard
# Last modified 22Jul17

# Program to plot sin(theta) and cos(theta) for 2.5 complete periods

print("Creating Plot...")

import numpy as np
import matplotlib.pyplot as plt

NPOINTS = 512
NPERIODS = 2.5
PERIOD = 2.0*np.pi

# Create array with 512 evenly space points between 0 and 2.5*2*pi (2.5 periods)
xvals = np.linspace(0, NPERIODS*PERIOD, NPOINTS)
f1, ax1 = plt.subplots()

ax1.plot(xvals, np.cos(xvals), 'b-') # Plot cos in blue
ax1.plot(xvals, np.sin(xvals), 'r-') # Plot sin in red

# Create title (LaTeX style editing)
plt.title(r'$\sin(\theta)$ and $\cos(\theta)$ vs. $\theta$')

# Create axes labes
plt.xlabel(r'$\theta$') # produces 'theta' 
plt.ylabel(r'$\cos(\theta)$ = blue, $\sin(\theta)$ = red')

# Save Figure
f1.savefig("p11_hw4_sincos.eps")

# Display figure with exit message
f1.show()
input("\nPress <Enter> to exit...\n")
