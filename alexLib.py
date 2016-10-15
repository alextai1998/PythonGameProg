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
    # A function that multiplies all the numbers in a list
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


def split_string(a):
    # A function that takes a string and creates a list with single words as elements
    # conditions: 'a' should be a string
    return a.split()


def print_frame(a):
    # A function that takes a list of strings and prints them, one per line, in a rectangular frame
    # conditions:'a' should be a list
    l_element = max(a, key=len)  # Finds the longest element
    x = len(l_element)  # Finds the length of the longest element
    max_stars = x + 7  # Determines the number of stars in the first/last row

    print("*" * max_stars)
    for each in a:
        num_space = max_stars - (len(each) + 3)  # Determines the number of spaces needed to align the last asterisk
        print("* " + each + " " * num_space + "*")
    print("*" * max_stars)


def count(a):
    # A function that counts how many times a word appears in a text
    # Returns a list with WORD in even positions, and OCCURRENCES in odd positions.
    # conditions: 'a' should be a string
    a = a.lower()
    list_a = a.split()
    list_b = []
    list_c = []

    counter = []

    for j in list_a:
        if j in list_b:
            counter[list_b.index(j)] += 1
        else:
            list_b.append(j)
            counter.append(1)

    for i in range(len(list_b)):
        list_c.append(list_b[i])
        list_c.append(counter[i])

    return list_c
