"""
This program creates the multiplication table (from 1 to 10) of a given number.
"""

number = input("Input a number: ")
print("Multiplication table of the number %s" % number)

for i in range(1, 11):
    product = int(number) * i
    print("%s x %s = %s" % (number, i, product))
