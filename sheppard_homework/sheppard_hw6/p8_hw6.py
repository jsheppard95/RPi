#!/usr/bin/env python3
# P8) Capacitor Potential Relaxation
# p8_hw6.py
# Author: Jackson Sheppard
# 05Aug17 - Created

# This program solves for and displays the electric potential in the
# neighbprhood of a 2-D parallel-plat capacitor using the relaxation method.
# It outputs an image corresponding to the square grid with its edges grounded
# and the capacitor plates set to +/-V. The colors in the image corresponding
# to the changing potential in space.

# graphics adapted from cmapimg.py
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import time

###############################################################################
# Adjustable Paramaters:
N = 10000              # max number of iterations
GRID = 200             # grid size
GAP = 0.22*GRID         # capacitor gap
WIDTH = 0.5*GRID       # capacitor plate width
THICKNESS = 0.06*GRID  # capacitor plate thickness
V = 6                  # Potential: top plate = +V, bottom plate = -V
###############################################################################

t0 = time.perf_counter()

X=GRID
Y=GRID

pvals = np.zeros((X,Y), dtype='uint') # array for image data
volt = np.zeros((X,Y), dtype='float') # array for actual voltage

# Solving differential equation by relaxation:
# 1) Set up boundary conditions in voltage array (edges @ V = 0, plates @ +/-V)
# 2) Create new array for current iteration: set each voltage in this array to
#    the average of the surrounding points in the previous array
# 3) Take difference between data before and after each iteration
# 4) Continue process until difference converges (stops changing) or reach N
#    (max number of iterations)

def load_boundary():
   """This function will load the boundary conditions into the voltage array
   corresponding to the grid. Called after each iteration to reset boundary
   conditions
   """
   # ground edges of grid:
   volt[0] = 0     # top edge
   volt[Y-1] = 0   # bottom edge
   volt[:,0] = 0   # left edge
   volt[:,X-1] = 0 # right edge
   
   # set charge on plates:
   volt[(Y//2)-(GAP//2),((X//2)-(WIDTH//2)):((X//2)+(WIDTH//2))] = V # top
   volt[(Y//2)+(GAP//2),((X//2)-(WIDTH//2)):((X//2)+(WIDTH//2))] = -V # bottom

# Now begin iteration process: interior only: not grounded edges
# grid space = indexing = 1
curr_iter = 0
print("Loading Boundary Conditions...")
load_boundary()
old_data = np.zeros((X,Y), dtype='float') # array to compare before/after iters
np.copyto(old_data, volt) # keeps arrays disconnected

print("Solving ODE by Relaxation...")
while curr_iter < N:
   volt = 0.25*(np.roll(volt, 1, axis=0) + np.roll(volt, -1, axis=0) + np.roll(volt, 1, axis=1) + np.roll(volt, -1, axis=1))
   load_boundary()
   diff = abs(volt - old_data)
   if np.all(diff <= 0.00015) == True:
      break 
   np.copyto(old_data, volt)
   curr_iter += 1
print("done")

# Now have voltage for each (x,y) in volt array
# Round, take absolute value and store in pvals array for image representation
# of solution

print("Creating and Plotting Color Map of Potential...")
for row in np.arange(Y):
   for col in np.arange(X):
      pvals[row][col] = abs(round(volt[row][col]))

f1, ax1 = plt.subplots()
picture = ax1.imshow(pvals, interpolation='none', cmap='jet')
ax1.axis('off')
f1.savefig('p8_hw6_cap3.eps')
f1.show()
print("done")
print('Time taken %.4f' % (time.perf_counter() - t0))

input("\nPress <Enter> to exit...\n")
