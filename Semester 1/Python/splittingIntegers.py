"""
This program takes a user input of an integer, and splits it into digits.
"""


number = int(input("Please enter a integer: "))
iteration = 0

while number != 0:
    number, residual = divmod(number, 10)
    iteration += 1
    print("Digit #%d = %d" % (iteration, residual))
