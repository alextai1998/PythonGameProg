"""
This program takes a non-negative integer from the user and repeatedly
adds all of its digits until the result has only one digit.
"""

x = input("Please enter a non-negative integer: ")
y = 0

while int(x) > 10:
    for i in range(len(x)):
        y += int(x[i])
    x = str(y)
    y = 0

print(x)
