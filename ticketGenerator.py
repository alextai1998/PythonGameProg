"""
This program passes the parameters from the console to determine the ticket you will receive.
------------------------------------------------------------------------------------------------
The 1st argument passed will be used to determine your speed.

The 2nd argument passed will determine if it is your birthday.
Please enter '1' if it is your birthday and '0' if it is not.
Arguments entered are always TRUE unless 0.
"""


import sys

# Converts the data entered into an integer
speed = int(sys.argv[1])


# Assigning boolean values into birthday
if int(sys.argv[2]) == 0:
    birthday = False
else:
    birthday = True


# Confirmation for the data entered
if birthday:
    print("Today is your birthday and you were driving at a speed of %d." % speed)
    print(" ")  # Printing blank line
else:
    print("Today is not your birthday and you were driving at a speed of %s." % speed)
    print(" ")  # Printing blank line


# Determining level of ticket if any
if birthday:
    if speed <= (60+5):
        print("You have no ticket")
    elif (61+5) <= speed <= (80+5):
        print("You have small ticket")
    else:
        print("You have big ticket")
else:
    if speed <= 60:
        print("You have no ticket")
    elif 61 <= speed <= 80:
        print("You have small ticket")
    else:
        print("You have big ticket")
