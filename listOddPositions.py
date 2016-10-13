"""
This program includes a function that returns all the elements on odd positions in a list.
"""


def odd_positions(a):
    # A function that returns a list of all the elements on odd positions in a list
    # conditions: 'a' should be a list
    mlist = [a[i] for i in range(1, len(a), 2)]
    return mlist
