"""
This program includes a function that takes a list of strings and prints them, one per line, in a rectangular frame.
"""


def print_frame(a):
    l_element = max(a, key=len)  # Finds the longest element
    x = len(l_element)  # Finds the length of the longest element
    max_stars = x + 7  # Determines the number of stars in the first/last row

    print("*" * max_stars)
    for each in a:
        num_space = max_stars - (len(each) + 3)  # Determines the number of spaces needed to align the last asterisk
        print("* " + each + " " * num_space + "*")
    print("*" * max_stars)


mlist = []

""" This section asks for the input """
while True:
        value = input("Enter the values of the list. (or enter nothing to stop.): ")
        if value == "":
            break
        mlist.append(value)  # list concatenation

print_frame(mlist)
