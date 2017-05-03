"""
This program walks the use through several yes or no questions that will determine whether or not the user
should change what he/she is doing. This program will return a final verdict after all the questions are answered.
"""

import sys

print("Should you keep doing whatever you're doing or change?")
print("Answer the following questions to find out!")
print(" ")  # Printing blank line


# Determines the verdict
if input("Are you happy? (y/n) ") == "y":
    sys.exit("Keep doing whatever you're doing!")
else:
    if input("Do you want to be happy? (y/n) ") == "y":
        sys.exit("Change something!")
    else:
        sys.exit("Keep doing whatever you're doing!")
