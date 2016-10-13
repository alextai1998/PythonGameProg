"""
This program serves as a library for all of the functions Alex wrote in class.
"""


def combine(a, b):
    # A function that combines two lists by alternating taking elements
    # It will also validate that the inputs have the same length before attempting to join them.#
    clist = []
    if len(alist) == len(blist):
        for i in range(0, len(a)):
            clist.append(a[i])
            clist.append(b[i])
    else:
        print("Error: arguments need to be in the same length!")
    return clist


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


def odd_positions(a):
    # A function that returns a list of all the elements on odd positions in a list
    # conditions: 'a' should be a list
    mlist = [a[i] for i in range(1, len(a), 2)]
    return mlist

