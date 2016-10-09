"""
This program includes a function that multiplies all the numbers in a list.
The function also skips non-numeric values.
"""


def multiply():
    product = 1
    mlist = []
    while True:
        value = input("Enter the value that should be multiplied. (or enter nothing to stop.): ")
        if value == "":
            break
        mlist.append(value)  # list concatenation

    for value in mlist:
        try:
            product *= int(value)
        except ValueError:
            continue

    print("The product is: %r" % product)

multiply()
