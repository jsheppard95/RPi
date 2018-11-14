#!/usr/bin/env python3

# P5) Mandelbrot Set
# filename: p5_hw5.py
# author: Jackson Sheppard
# Last modified: 21Jul17

# Program will plot a region of the complex plane that includes the mandelbrot
# set. The mandelbrot set will be colored black while the surrounding region
# will be colored

from PIL import Image

print("Please wait, fractal image loading...")

# image size:
X = 512
Y = 384

# Create new image:
im = Image.new("RGB", (X, Y), "black")

# Pixel coordinate system: (0,0) = top left, (512, 384) = bottom right
# Want to change to a xy cartesian coordinate system with (0,0) at center, x increasing to the right, and y increasing up.

def transformx(x, xres):
   x -= xres/2
   x *= (4/xres)
   return x

def transformy(y, yres):
   y -= yres/2
   y *= (4/yres)
   y = -y
   return y

# Iterate through pixels in now empty (black) image
# Mandelbrot set: z_n+1 = z_n^2 + c remains bounded for all n, then
# c is in the mandelbrot set
for i in range(X):
   x = transformx(i, X)
   for j in range(Y):
      y = transformy(j, Y)
      c = complex(x, y)
      if abs(c) > 2: # upper radius = 2 (derivation on wikipedia)
         c = 2
      z = complex(0,0) # loop until abs(z) no longer less than two
      count = 0
      while count < 250 and abs(z) < 2: # max_iterations = 250
         z = z**2 + c
         count += 1
      # Set pixel if sequence diverged:
      if abs(z) > 2:
         px = im.load()
         px[i, j] = (239, 222, 205)

print("done")
im.save('p5_hw4_mandelbrot.ps')
im.show()
