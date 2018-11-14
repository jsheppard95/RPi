#!/usr/bin/env python3
# P5) Factoring Numbers
# filename: p5_hw3.py
# This program prompts the user to enter and integer, converts the type to an appropriate variable, and prints out the prime factors of the number:

import numpy
# a) Prompt user to enter an integer
while True:
   try:
      integer = int(input("Enter a number: "))
      break
   except ValueError:
      print("Not a valid number. Try again: ")
print(integer)

# Function to determine if integer n is prime
def is_prime(n):
   """Determines if integer n is prime: Returns true if prime, false if not prime
   """
# initially assume number not prime, iterate through integers less than n to find possible divisors: if one is found, number not prime: return false. Otherwise, number prime: return true
   result = False
   if n < 2:
      return result
   else:
      for i in numpy.arange(2, n):
         if (n % i) == 0:
            return result
   result = True
   return result

# Testing is_prime(n):
#for i in range(1, 25):
#   print(i, is_prime(i))

# Determine prime factors:
prime_factors = []
for i in numpy.arange(2, integer):
   if (is_prime(i) == True) and (integer % i == 0):
      prime_factors.append(i)

# Print out prime factors:
if len(prime_factors) > 0:
   print("Prime Factors:")
   for i in prime_factors:
      print(i, end=' ')
   print('\n')
else:
   print(integer, 'is prime.')
