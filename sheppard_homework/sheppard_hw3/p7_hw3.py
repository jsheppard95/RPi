#!/usr/bin/env python3
# P7) Execution Speed
# filename: p7_hw3.py
# Determine execution time of various python commands inside loops:

import time
print("Execution times:")
print("")

def print_output(command_str, num_cycles, time_tot, time_one):
   print("Command/Action:", command_str)
   print(num_cycles, end=' iterations: ')
   print(time_tot, 'seconds')
   print("Single command:", time_one, 'seconds')
   print("")

num_iters = 2000000 # (2 million)

# a) pass statement:
t0_pass = time.perf_counter()
for i in range(num_iters):
   pass
t1_pass = time.perf_counter()
dt_pass_tot = t1_pass - t0_pass
dt_pass_one = dt_pass_tot / num_iters
print_output('pass', num_iters, dt_pass_tot, dt_pass_one)

# float variables:
float1 = 1.2
float2 = 3.4

# b) Addition of two float variables:
t0_add_float = time.perf_counter()
for i in range(num_iters):
   float_sum = float1 + float2
t1_add_float = time.perf_counter()
dt_add_tot = t1_add_float - t0_add_float
dt_add_one = dt_add_tot / num_iters
print_output('Add two floats', num_iters, dt_add_tot, dt_add_one)

# c) Multiplication of two float variables:
t0_mult_float = time.perf_counter()
for i in range(num_iters):
   float_mult = float1 * float2
t1_mult_float = time.perf_counter()
dt_mult_tot = t1_mult_float - t0_mult_float
dt_mult_one = dt_mult_tot / num_iters
print_output('Multiply two floats', num_iters, dt_mult_tot, dt_mult_one)

# d) Division of two float variables
t0_div_float = time.perf_counter()
for i in range(num_iters):
   float_div = float1 / float2
t1_div_float = time.perf_counter()
dt_div_tot = t1_div_float - t0_div_float
dt_div_one = dt_div_tot / num_iters
print_output('Divide two floats', num_iters, dt_div_tot, dt_div_one)

# e) Integer division of two variables:
int1 = 15
int2 = 4
t0_div_int = time.perf_counter()
for i in range(num_iters):
   int_div = int1 // int2
t1_div_int = time.perf_counter()
dt_intdiv_tot = t1_div_int - t0_div_int
dt_intdiv_one = dt_intdiv_tot / num_iters
print_output('Integer division of two integers', num_iters, dt_intdiv_tot, dt_intdiv_one)

# f) Appending one number to a list
list_small = [2]
t0_append_small = time.perf_counter()
for i in range(num_iters):
   list_small.append(2)
t1_append_small = time.perf_counter()
dt_appendsmall_tot = t1_append_small - t0_append_small
dt_appendsmall_one = dt_appendsmall_tot / num_iters
print_output('Append one number to small list (initially one element)', num_iters, dt_appendsmall_tot, dt_appendsmall_one)

list_large = list(range(num_iters))
t0_append_large = time.perf_counter()
for i in range(num_iters):
   list_large.append(2)
t1_append_large = time.perf_counter()
dt_appendlarge_tot = t1_append_large - t0_append_large
dt_appendlarge_one = dt_appendlarge_tot / num_iters
print_output('Append one number to large list (initially 2000000 elements)', num_iters, dt_appendlarge_tot, dt_appendlarge_one)

# g) Call to function that does nothing (contains only pass statement)
def nothing():
   pass
t0_func_pass = time.perf_counter()
for i in range(num_iters):
   nothing()
t1_func_pass = time.perf_counter()
dt_funcpass_tot = t1_func_pass - t0_func_pass
dt_funcpass_one = dt_funcpass_tot / num_iters
print_output('Call to function with pass statement', num_iters, dt_funcpass_tot, dt_funcpass_one)

# h) Call to function that adds to floats:
def add_floats(float1, float2):
   float_sum = float1 + float2
   return float_sum
t0_func_add = time.perf_counter()
for i in range(num_iters):
   add_floats(float1, float2)
t1_func_add = time.perf_counter()
dt_funcadd_tot = t1_func_add - t0_func_add
dt_funcadd_one = dt_funcadd_tot / num_iters
print_output('Call to function that adds two floats', num_iters, dt_funcadd_tot, dt_funcadd_one)

