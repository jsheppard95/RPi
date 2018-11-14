#!/usr/bin/env python3

# P3) String Processing
# filename: p3_hw3.py
# Note: counting all spaces and punctuation as characters in input string

# a) Prompt user for string (3+ word)
string = input('Enter a string with at least 3 words: ')
word_list = string.split(' ')

# b) Reject string if string and reprompt if fewer than 3 word:
while len(word_list) < 3:
   print('String rejected')
   string = input('Enter string with at least 3 words: ')
   word_list = string.split(' ')

# c) Print words in string, one per line:
print('')
print('Words in the string:')
for i in word_list:
   print(i)

# d) Print first three characters of the string:
print('')
print('First three characters:')
print(string[0:3])

# e) Print last three characters of string:
print('')
print('Last three characters:')
print(string[(len(string) - 3):len(string)])

# f) Print first half of the string:
print('')
print('First half of string (including boundary):')
if (len(string) % 2) == 0: # even number of char's
   print(string[:(len(string) // 2)])
else: # odd number of char's
   print(string[:((len(string) // 2) + 1)])

# g) Print the last half of string:
print('')
print('Last half of string (including boundary):')
print(string[(len(string) // 2):])

# h) Print the string with the words in reverse order:
print('')
print('String with words in reverse order:')
for i in range(len(word_list) - 1, -1, -1):
   print(word_list[i], end=' ')
print('\n')

# i) Print the string with the words alphabetized:
print('')
print('String with words alphabetized:')
alpha_word_list = sorted(word_list, key=str.lower)
for i in alpha_word_list:
   print(i, end=' ')
print('\n')

# j) Prints each character in the string, one per line:
print('')
print('Characters in the string:')
for i in range(len(string)):
   print(string[i])

# k) Print hexadecimal values for each character in string, one per line:
print('')
print('Hexadecimal values for each character in string:')
for i in range(len(string)):
   hex_val = hex(ord(string[i]))
   print(hex_val)
