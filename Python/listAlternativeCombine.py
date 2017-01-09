"""
A function that combines two lists by alternating taking elements
It will also validate that the inputs have the same length before attempting to join them.
"""


def combine(a, b):
    clist = []
    if len(alist) == len(blist):
        for i in range(0, len(a)):
            clist.append(a[i])
            clist.append(b[i])
    else:
        print("Error: arguments need to be in the same length!")
    return clist
