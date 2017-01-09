"""
This program passes the parameters from the console to determine the status of two monkeys.
The two monkeys can either be smiling or not smiling and if both monkeys are smiling or if
neither of the monkeys are smiling then the program will tell us that we are in trouble.

Arguments entered are always TRUE unless 0.
"""


import sys


# Converting parameters into integers and assigning status of Monkey A
if int(sys.argv[1]) == 0:
    monkeyA = "not smiling"
else:
    monkeyA = "smiling"

# Converting parameters into integers and assigning status of Monkey B
if int(sys.argv[2]) == 0:
    monkeyB = "not smiling"
else:
    monkeyB = "smiling"


# Confirmation for the data entered
print("You have stated that Monkey A is %s and Monkey B is %s." % (monkeyA, monkeyB))

# Determining if we are in trouble by using if testing
if monkeyA == monkeyB:
    print("We are in trouble.")
else:
    print("We are fine.")
