#!/usr/bin/env python3

# P12) Surface Plot
# filename: p12_hw4.py
# author: Jackson Sheppard
# Last modified 22Jul17

# program to plot the function z(x,y) = sin(x)cos(y) for 2.5 periods on the x
# and y axes

print("Creating Plot...")

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

NPOINTS = 512
NPERIODS = 2.5
PERIOD = 2.0*np.pi

# Create arrays (x and y) with 512 evenly spaced points between 0 and 2.5*2*pi
xvals = np.linspace(0, NPERIODS*PERIOD, NPOINTS)
yvals = np.linspace(0, NPERIODS*PERIOD, NPOINTS)

# Create grid of x and y
X, Y = np.meshgrid(xvals, yvals)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # used for 3d plotting

# function to plot
def z_func(x, y):
   z = np.sin(x)*np.cos(y)
   return z

# Get z values: zip together x and y arrays to create array of (x,y) tupples
# and then iterate through tuple to get array of z values
zvals = np.array([z_func(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zvals.reshape(X.shape)

# Plot z(x,y) vs x and y
ax.plot_surface(X, Y, Z)

# Set Axes Labels and Title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z = sin(x)cos(y)')
plt.title('Surface Plot of z = sin(x)cos(y)')

# Save figure
fig.savefig("p12_hw4_surfaceplot.eps")

# Show figure with exit message
fig.show()
input("\nPress <Enter> to exit...\n")

