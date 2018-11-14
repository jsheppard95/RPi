#!/usr/bin/env python3
# P9) Sine Function
# filename: p9_hw3.py


# a) Prompt user for angle in degree:
angle_deg = float(input("Enter angle in degrees: "))

# b) Prompt user to enter number of terms to sum in a series:
n = int(input("Enter number of terms in series: "))

# c) Calculate sine of angle using taylor series expansion
def factorial(n):
   """Calculates factorial of integer n
   """
   if n == 1:
      return 1
   if n == 0:
      return 1
   next_num = n - 1
   total = n * next_num
   while True:
      if next_num == 1:
         break
      next_num -= 1
      total *= next_num
   return total

def sind(angle_deg, num_terms):
   """Approximates sine of angle in degrees using taylor series with n terms
   angle_deg: angle in degrees
   num_terms: number of terms to use in series
   """
   angle = angle_deg*3.141592653589793/180
   tot = 0
   i = 1
   while i <= num_terms:
      term = ((-1)**(i-1))*(angle**((2*i)-1))/factorial((2*i)-1) # taylor series
      tot += term
      i = i + 1
   return tot

approx_sin = sind(angle_deg, n)
print("")
print("Series Approximation:", approx_sin)

# d) Calculate sine of angle using math.sine
import math
angle = angle_deg*math.pi/180
actual_sin = math.sin(angle)
print("Value using math.sin:", actual_sin)

# e) comparison
print("")
ratio = approx_sin/actual_sin
print("Ratio (approximate/actual):", ratio)
diff = abs(approx_sin - actual_sin)
print("Absolute Difference:", diff)
