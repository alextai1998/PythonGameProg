"""
This program takes a word from the user and reverses the characters using for loops
"""

x = input("Please enter a word you want reversed: ")

for i in range(len(x)-1, -1, -1):
    print(x[i])
