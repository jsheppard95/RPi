#!/usr/bin/env python3
# P6) Dictionaries and Databases
# filename: p6_hw3.py

# a) Read in csv file and add each line as element of list
f = open('p6_hw3.csv', 'r')
line_list = f.readlines()
line_list_fix = [] # take out '/n'
for line in line_list:
   line_fix = line.rstrip('\n')
   line_list_fix.append(line_fix)
#print(line_list_fix)

# b) Store file info into list of dictionaries
file_info = [] # will be 2d list:[[file_line1],[file_line2], [file_line3]]
for string in line_list_fix:
   info = string.split(',')
   file_info.append(info)
#print(file_info) 
# Organize 2d list with dictionaries:
file_dict = []
for list_info in file_info:
   dict1 = {'last':list_info[0], 'first':list_info[1], 'color':list_info[2], 'food':list_info[3], 'subject':list_info[4], 'physicist':list_info[5]}
   file_dict.append(dict1)
#print(file_dict)

# c) Print list of keys for user:
print('Keys to choose:')
list_of_keys = list(file_dict[0].keys())
for i in list_of_keys:
   print(i)

# d) Prompt user to enter key:
print("")
key = input("Please enter a key, enter q to quit: ")

# e) Print names & f) Allow user to continue until finished
print("")
while key != 'q':
   for person in file_dict:
      print(person['last'], end=', ')
      print(person['first'], end=': ')
      print(person[key])
   print("")
   key = input("Please enter a key, enter q to quit: ")
