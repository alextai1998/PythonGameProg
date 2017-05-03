"""
This program takes a word from the user and checks if it is a palindrome
"""

import sys

x = str(sys.argv)

if x == x[::-1]:
    palindrome = True
else:
    palindrome = False

if palindrome:
    print("The word '%s' is a palindrome!" % x)
else:
    print("The word '%s' is not a palindrome!" % x)
