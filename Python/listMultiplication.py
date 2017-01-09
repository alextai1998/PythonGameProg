"""
This program includes a function that multiplies all the numbers in a list.
The function also skips non-numeric values.
"""


def multiply(a):
    # A function that multiplies all the numbers in a list.
    # The function also skips non-numeric values.
    # conditions: 'a' should be a list
    product = 1
    for value in a:
        try:
            product *= int(value)
        except ValueError:
            continue
    return product

