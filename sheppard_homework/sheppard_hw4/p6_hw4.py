#!/usr/bin/env python3

# P6) PostScript Flower
# filename: p6_hw4.py
# author: Jackson Sheppard
# Last modified: 22Jul17

# Program will input from the user the number of petals and then write to the
# disk a postscript program that draws a flower with the specified number of
# petals

# Input number of petals: Ensure less than 100
num_petals = int(input("Enter number of petals (as integer): "))
while num_petals >= 100:
   print("Too many petals, please enter less than 100")
   num_petals = int(input("Enter number of petals (as integer): "))

petal_spacing = 360/num_petals

# Create output file for ps program
outfile = open('p6_hw4_petal.ps', 'w') 
output = """
%!PS
%
% 05May16  Everett Lipman
%

%
% draw petal scaled by xscale and yscale, rotated by angle.
%
/petal  % xscale yscale angle petal
   {
   /petalcol [ 0.8 0 0 ] def
   /ep1 [ 0 0 ] def
   /ep2 [ 0 100 ] def
   /cp1 [ 55 65 ] def
   /cp2 [ 10 95 ] def
   /ap {aload pop} def
   gsave
   petalcol ap setrgbcolor
   0 setlinewidth
   rotate  % use angle from stack
   scale   % use xscale and yscale from stack

   ep1 ap moveto
   cp1 ap cp2 ap ep2 ap curveto
   cp2 ap exch neg exch
   cp1 ap exch neg exch
   ep1 ap curveto closepath fill

   grestore
   } def

gsave
   306 500 translate


"""

# create array of angles of petal, start at 0
angles = [0]
for i in range(num_petals-1):
   angles.append(angles[i] + 360/num_petals)

# add draw petal command to ps program for each eangle
for angle in angles:
   output += "   1 1 " + str(angle) + " petal\n"

# complete ps program
output += "grestore\n"
output += "\n"
output += "showpage\n"

# write ps program to output file
outfile.write(output)

outfile.close()
