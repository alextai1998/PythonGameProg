"""
This program includes a function that returns all the elements on odd positions in a list.
"""


def odd_positions(a):
    for i in range(1, len(a), 2):
        print(a[i])

mlist = []

while True:
        value = input("Enter the values of the list. (or enter nothing to stop.): ")
        if value == "":
            break
        mlist.append(value)  # list concatenation

odd_positions(mlist)  # Calling the function with the list as the argument
