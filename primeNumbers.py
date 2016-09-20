"""
This program asks the user to enter a number (n), and the program returns the first nth prime numbers.
"""


# Initializing variables
n = int(input("Please enter the number of prime numbers: "))
notPrime = False  # Used as flag
iteration = 0
x = 2


while iteration < n:  # Ends when the iteration reaches the nth prime number
    x += 1
    if iteration == 0:
        print('2')  # Forcibly print 2
        iteration += 1
    for i in range(2, x):
        if x % i == 0:
            notPrime = True  # Flagging
            break  # Skips over non-prime numbers
    if not notPrime:
        print(x)
        iteration += 1
    notPrime = False  # Resetting flag
