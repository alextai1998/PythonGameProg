"""
This program includes a function that prints menus in the terminal.
The input is a list of options, and the output is the option selected by the user.
"""

import sys


def menu_input(a):
    print("The options are: ")
    for i in range(len(a)):
        print("     %r. " % (i+1) + a[i])
    pref = input("What is your preference (1-%r)? Or press X to exit. " % len(a))

    if pref == "X" or "x":
        sys.exit()
    else:
        print(a[int(pref)-1])


menu = []

""" This section asks for the input """
while True:
        value = input("Add the items of the menu one by one. (or enter nothing to stop.): ")
        if value == "":
            break
        menu.append(value)  # list concatenation

menu_input(menu)
