"""
This program receives an integer N via user input, and returns TRUE if the integer is within 10 to 100 or if the
integer is 200.
"""

value = input("Please enter an integer. ")

# Validates input
valueFloat = float(value)
valueInt = int(valueFloat)

# Determines the conditions for the program
if valueFloat == valueInt:
    if 10 < valueInt < 100 or valueInt == 200:
        print("True")
    else:
        print("False")
else:
    print("Please enter a valid number(INTEGER)")
