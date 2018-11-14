#!/usr/bin/env python3
# P8) Fibonacci Numbers
# filename: p8_hw3.py

# takes in command line argument single number n:
# prints out first n fibonacci number: 1, 1, 2, 3, 5 ...(n numbers)

import sys

print()
print('The argument list is:  %s' % repr(sys.argv))
print('The argument count is: %d' % len(sys.argv))
print()

arg_list = sys.argv
print(arg_list)
n = int(arg_list[1])

fib_list = [1, 1]
curr = 1
prev = 1
while len(fib_list) < n:
   next_num = curr + prev
   fib_list.append(next_num)
   prev = curr
   curr = next_num

count = 1
line = ""
for num in fib_list:
   num_str = str(num)
   line = line + num_str + ' '
   if len(line) == 75:
      print(line)
      line = ""
print(line)
