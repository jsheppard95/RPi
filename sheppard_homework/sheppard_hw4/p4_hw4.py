#!/usr/bin/env python3

# P4) 3-4-5 Right Triangle
# filename: p4_hw4.py
# author: Jackson Sheppard
# Last modified: 21Jul17

# Program will draw a 3-4-5 right triangle using raster graphics and save the 
# image an .eps file

from PIL import Image, ImageDraw
import math

# Create new image:
im = Image.new("RGB", (512, 410), "white")
draw_obj = ImageDraw.Draw(im)

# Set image border:
lower = 48
upper = 48
right = 67
left = 27

# Draw horizontal side of triangle
draw_obj.line([(left, 410-lower), (512-right,410-lower)], fill="blue", width=10)

ang_y = math.asin(3/5) # angle across from vertical side of triangle
ang_x = 90 - ang_y # angle across from horizontal side of triangle
tri_height =(512-left-right)*math.tan(ang_y)

# Draw vertical side of triangle
draw_obj.line([(512-right,410-lower), (512-right, 410-lower-tri_height)], fill="blue", width=10)
# Draw hypotenuse
draw_obj.line([(512-right, 410-lower-tri_height), (left, 410-lower)], fill="blue", width=10)

# Save image
im.save('p4_hw4_rt345.eps')
im.show()
